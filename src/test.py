# from sqlOps.users.sqlRead import sqlAuthenticate
# from sqlOps.users.sqlWrite import sqlRemoveAccount, sqlCreateAccount
# from sqlOps.users.sqlDev import sqlViewTable
# from routers.users import create_user
# from lib.models import ProfileType, DateType, jwtPayload, GenerateID
# from minioDB.conn import s3
# from sqlOps.posts.sqlRead import sqlGetPost, sqlGetProfilePosts
from lib.models import GenerateID
from sqlOps.posts.sqlWrite import sqlAddPost
from lib.models import PostType
from datetime import datetime

# birthday = DateType(day='18', month='June', year='2002')
# profile = ProfileType(
#                     userID='gh37xp0f7b5s98bh',
#                     username='Will',
#                     password='password',
#                     birthday=birthday,
#                     email='willtdougherty@gmail.com',
#                     followCount=0)
# sqlRemoveAccount('9ObnGt8Rwa4M5I2G')
# sqlViewTable()

# payload = jwtPayload(
#     iss='localhost',
#     sub='gh37xp0f7b5s98bh',
#     aud='localhost',
#     iat=0,
#     exp=0,
#     nbf=0
# )
# sqlAuthenticate('WillDougherty', 'passwosrd')
print(GenerateID(16))
# print(sqlGetPost('984WAWyDxKWDW8ix'))
# print(sqlGetProfilePosts('7Pp2bzGeGWJDzz61'))

dt = datetime.now()
formatted_date_time = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
print(formatted_date_time)
# new_post = PostType(
#     postID=GenerateID(16),
#     userID="tYzR36S2gwdYkpPR",
#     username="LebronJames",
#     posted_at=formatted_date_time
# )
# sqlAddPost(new_post)