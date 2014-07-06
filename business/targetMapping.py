class ModelMapping:
	def targetMapping(self, targets):
		result=[]
		for target in targets:
			result.append({
				"id"			: str(target.id), 
				"title"			: target.title, 
				"description"	: target.getShortDescription(), 
				"tasksNumber"	: target.taskCount(), 
				"endPercent"	: target.getEndPercent(), 
				"owner"			: {
									"name"		: target.owner.name,
									"img"		: "/static/images/users/" + str(target.owner.getUrlImage())
								}
				})
		return result
