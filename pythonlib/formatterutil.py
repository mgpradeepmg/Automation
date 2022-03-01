def extractvalue(res, val):
    return res["body"][val]

def return_user_body(body):
    for k, v in body.items():
        body[k]=body[k]+"1"
    return body


# if __name__=='__main__':
#     userbody = {"name": "tesmon-testnew3asdfaasdfsdf", "job": "new4asdfasdfafadfd" }
#     final=return_user_body(userbody)
#     print(final)