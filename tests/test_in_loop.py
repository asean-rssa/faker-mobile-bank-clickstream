from faker import Faker
from faker_mobile_bank_clickstream import ClickstreamProvider
import time

fake = Faker()
fake.add_provider(ClickstreamProvider)

while(True):
  time.sleep(1)
  sessionData = fake.session_clickstream(rand_session_max_size= 25, min_user_id= 1, max_user_id=100000)
  for s in sessionData:
    print(f"ip: {s['ip']}, user_id: {s['user_id']}, event_name: {s['event_name']}")
  print("------------------------------------------------------------------")

