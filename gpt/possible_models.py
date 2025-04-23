from get_client import client

models = client.models.list()

for model in models:
    # print(vars(model)) # vars(): 객체의 모든 속성을 dict로 표시
    print(model.id)