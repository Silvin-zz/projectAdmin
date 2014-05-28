

import logging
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
from django.conf         import settings
from principal.models    import driveConfiguration
import json
import httplib2
import oauth2client
# ...


# Path to client_secrets.json which should contain a JSON document such as:
#   {
#     "web": {
#       "client_id": "[[YOUR_CLIENT_ID]]",
#       "client_secret": "[[YOUR_CLIENT_SECRET]]",
#       "redirect_uris": [],
#       "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#       "token_uri": "https://accounts.google.com/o/oauth2/token"
#     }
#   }
CLIENTSECRETS_LOCATION = settings.BASE_DIR + "/auth/client_secrets.json"
REDIRECT_URI = 'http://127.0.0.1:8000/document/show'
SCOPES = [
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    # Add other requested scopes.
]

class GetCredentialsException(Exception):
  """Error raised when an error occurred while retrieving credentials.

  Attributes:
    authorization_url: Authorization URL to redirect the user to in order to
                       request offline access.
  """

  def __init__(self, authorization_url):
    """Construct a GetCredentialsException."""
    self.authorization_url = authorization_url


class CodeExchangeException(GetCredentialsException):
  """Error raised when a code exchange has failed."""


class NoRefreshTokenException(GetCredentialsException):
  """Error raised when no refresh token has been found."""


class NoUserIdException(Exception):
  """Error raised when no user ID could be retrieved."""


def get_stored_credentials(user_id):

  objs        = driveConfiguration()
  credential  = objs[0].credential
  return oauth2client.client.Credentials.new_from_json(credential)


  """Retrieved stored credentials for the provided user ID.

  Args:
    user_id: User's ID.
  Returns:
    Stored oauth2client.client.OAuth2Credentials if found, None otherwise.
  Raises:
    NotImplemented: This function has not been implemented.
  """
  # TODO: Implement this function to work with your database.
  #       To instantiate an OAuth2Credentials instance from a Json
  #       representation, use the oauth2client.client.Credentials.new_from_json
  #       class method.
  raise NotImplementedError()


def store_credentials(user_id, credentials):

  objs= driveConfiguration.objects()

  if(len(objs) ==0):
    obj= driveConfiguration()
  else:
    obj=objs[0]

  obj.credential=credentials.to_json()
  obj.active=True
  obj.save()
  print("Terminamos de Guardar la credencial")




  """Store OAuth 2.0 credentials in the application's database.

  This function stores the provided OAuth 2.0 credentials using the user ID as
  key.

  Args:
    user_id: User's ID.
    credentials: OAuth 2.0 credentials to store.
  Raises:
    NotImplemented: This function has not been implemented.
  """
  # TODO: Implement this function to work with your database.
  #       To retrieve a Json representation of the credentials instance, call the
  #       credentials.to_json() method.
  #raise NotImplementedError()


def exchange_code(authorization_code):
  """Exchange an authorization code for OAuth 2.0 credentials.

  Args:
    authorization_code: Authorization code to exchange for OAuth 2.0
                        credentials.
  Returns:
    oauth2client.client.OAuth2Credentials instance.
  Raises:
    CodeExchangeException: an error occurred.
  """
  print("traemos el Autorization code: " + authorization_code)
  flow = flow_from_clientsecrets(CLIENTSECRETS_LOCATION, ' '.join(SCOPES))
  print(flow)
  flow.redirect_uri = REDIRECT_URI
  try:
    print("Momento de Solicitar la credencial")
    credentials = flow.step2_exchange(authorization_code)
    print("Terminamos de solicitar las credenciales ::::::::::::::::::::::::::")
    return credentials
  except FlowExchangeError, error:
    print("Ocurrio un error al momento de solicitar las credenciales")
    logging.error('An error occurred: %s', error)
    raise CodeExchangeException(None)


def get_user_info(credentials):
  """Send a request to the UserInfo API to retrieve the user's information.

  Args:
    credentials: oauth2client.client.OAuth2Credentials instance to authorize the
                 request.
  Returns:
    User information as a dict.
  """
  print("Iniciamos la solicitud de datos del usuario")
  http = httplib2.Http()
  http = credentials.authorize(http)
  user_info_service= build('oauth2', 'v2', http=http)
  # user_info_service = build(
  #     serviceName='oauth2', version='v2',
  #     http=credentials.authorize(httplib2.Http()))
  print("continuamos.........")
  user_info = None
  try:
    print("Traemos los datos del usuario")
    user_info = user_info_service.userinfo().get().execute()
  except errors.HttpError, e:
    print("ocurrio un error al momento de solicitar los datos :(")

    logging.error('An error occurred: %s', e)
  if user_info and user_info.get('id'):
    return user_info
  else:
    raise NoUserIdException()


def get_authorization_url(email_address, state):
  """Retrieve the authorization URL.

  Args:
    email_address: User's e-mail address.
    state: State for the authorization URL.
  Returns:
    Authorization URL to redirect the user to.
  """
  flow = flow_from_clientsecrets(CLIENTSECRETS_LOCATION, ' '.join(SCOPES))
  flow.params['access_type']      = 'offline'
  flow.params['approval_prompt']  = 'force'
  flow.params['user_id']          = email_address
  flow.params['state']            = state
  return flow.step1_get_authorize_url(REDIRECT_URI)

def getAPIService():
  print("Iniciamos la busqueda")
  objs       = driveConfiguration.objects()
  obj        = objs[0]
  if(obj.active==True):
    print("ya hay una credencial")
    credentials=oauth2client.client.Credentials.new_from_json(obj.credential)
    print("Obtuvimos la crdencial")
  else:
    print("Token:" + objs[0].token)
    credentials =get_credentials(objs[0].token,2)
  print(credentials)
  http = httplib2.Http()
  http = credentials.authorize(http)
  return build('drive', 'v2', http=http)
  
  
  
def getAPICredential():
  print("Iniciamos la busqueda")
  objs       = driveConfiguration.objects()
  obj        = objs[0]
  if(obj.active==True):
    print("ya hay una credencial")
    credentials=oauth2client.client.Credentials.new_from_json(obj.credential)
    print("Obtuvimos la crdencial")
  else:
    print("Token:" + objs[0].token)
    credentials =get_credentials(objs[0].token,2)
  print(credentials.to_json())
  return credentials


def get_credentials(authorization_code, state):
  """Retrieve credentials using the provided authorization code.

  This function exchanges the authorization code for an access token and queries
  the UserInfo API to retrieve the user's e-mail address.
  If a refresh token has been retrieved along with an access token, it is stored
  in the application database using the user's e-mail address as key.
  If no refresh token has been retrieved, the function checks in the application
  database for one and returns it if found or raises a NoRefreshTokenException
  with the authorization URL to redirect the user to.

  Args:
    authorization_code: Authorization code to use to retrieve an access token.
    state: State to set to the authorization URL in case of error.
  Returns:
    oauth2client.client.OAuth2Credentials instance containing an access and
    refresh token.
  Raises:
    CodeExchangeError: Could not exchange the authorization code.
    NoRefreshTokenException: No refresh token could be retrieved from the
                             available sources.
  """
  email_address = 'singleprojects@gmail.com'

  try:
    print("Solicitando Credenciales para "+ email_address)
    credentials = exchange_code(authorization_code)
    print("Guardamos las credenciales::::::")
    print("Vamos por el User Info")
    #user_info = get_user_info(credentials)
    #email_address = user_info.get('email')
    #user_id = user_info.get('id')
    if credentials.refresh_token is not None:
      print("Guardamos las nuevas credenciales")
      store_credentials("10", credentials)
      return credentials
    else:
      print("Obtenemos las credenciales de la base de datos")
      credentials = get_stored_credentials("10")

      if credentials and credentials.refresh_token is not None:
        return credentials
  except CodeExchangeException, error:
    logging.error('An error occurred during code exchange.')
    # Drive apps should try to retrieve the user and credentials for the current
    # session.
    # If none is available, redirect the user to the authorization URL.
    print("Debemos ir a esta URL :(")

    error.authorization_url = get_authorization_url(email_address, state)
    print(error.authorization_url)
    print(error)
  except NoUserIdException:
    logging.error('No user ID could be retrieved.')
  # No refresh token has been retrieved.
  authorization_url = get_authorization_url(email_address, state)
  print(NoRefreshTokenException(authorization_url))