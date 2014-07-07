class ModelMapping:
	def targetMapping(self, targets):
		result=[]
		for target in targets:
			result.append({
				"id"			: str(target.id), 
				"title"			: target.title, 
				"description"	: target.description, 
				"shortdesc"		: target.getShortDescription(), 
				"tasksNumber"	: target.taskCount(), 
				"endPercent"	: target.getEndPercent(),
				"datestart"		: str(target.datestart.date()),
				"dateend"		: str(target.dateend.date()), 
				"code"			: target.code,
				"targettype"	: str(target.targettype.id),
				"finished"		: target.finished,
				"owner"			: {
									"name"		: target.owner.name,
									"img"		: "/static/images/users/" + str(target.owner.getUrlImage()),
									"id"		: str(target.owner.id)
								}
				})
		print("El resultado es:::::D")
		print("saludos")
		return result
