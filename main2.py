import scratchattach as sa

user = sa.login_by_id(".eJxVUEFOwzAQ_IvPbYhTO617K0jAhSJ6AHGK7PUmMWnsKHZUAeLvrKVeelvNzszO7C9bIs5ej8j2TMd-dEl7G2HWCXq2Yo1eUt9kTuMsUXgptmojdxXtEsYEIQwuay9hHtDeKoyGAX2WZQx9cqCTC764LmJxwul8Be-vZPINNJBItkKpDchKYi0AUe9EDWpXW0BlAeR--w4P3etwnGKEU_2iH0NQfP388f30Rjbn0Dm_dhM5CVVU5bbgShSK54xn7btFdzk4nVox-0VAaJIb8Sf4DB9GnCnZ3REvzSd1u23W06uIZBG5oVwlr40uheLcSCNbi1BDy7FUvOLGGmR__2usdkw:1vD4Lq:p8SKJzbjX85BuG9vtowr8IDGiRg", username="ashmitandscratch")
print("Signed in!")
cloud = user.connect_scratch_cloud(1232273203)
print("Cloud connected!")
while True:
    var = cloud.get_var("REQUEST")
    if var != "":
        print("REQUEST RECEIVED:", var)
        cloud.set_var("RESPONSE", int(var) * 2)
        cloud.set_var("REQUEST", "")
