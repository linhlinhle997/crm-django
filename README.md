# crm-djangoCancel changes

# Model managers
# to create a new car
Lead.objects.create(first_name="Linh", last_name="Le", age=25, agent=admin@gmail.com)

# Querysets 
# query for all leads in the databse
Lead.objects.all()
# query for lead with the make equal to "Linh"
Lead.objects.filter(first_name="Linh")
# query for lead with a age greater than 20
Lead.objecs.filter(age__gt=20)
# get one Agent
Agent.objects.get(user__email="admin@gmail.com")
Agent.objects.get(user=1) = Agent.objects.get(user__id=1)
# get one Lead
Lead.objects.get(agent=1) = Lead.objects.get(agent__user=1)