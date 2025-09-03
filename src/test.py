from sqlOps.sqlRead import sqlAuthenticate
from sqlOps.sqlWrite import sqlRemoveAccount, sqlCreateAccount
from sqlOps.sqlDev import sqlViewTable
from routers.users import create_user
from lib.models import ProfileType, DateType, jwtPayload

# birthday = DateType(day='18', month='June', year='2002')
# profile = ProfileType(
#                     userID='gh37xp0f7b5s98bh',
#                     username='Will',
#                     password='password',
#                     birthday=birthday,
#                     email='willtdougherty@gmail.com',
#                     followCount=0)
# sqlRemoveAccount('9ObnGt8Rwa4M5I2G')
sqlViewTable()

payload = jwtPayload(
    iss='localhost',
    sub='gh37xp0f7b5s98bh',
    aud='localhost',
    iat=0,
    exp=0,
    nbf=0
)
sqlAuthenticate('WillDougherty', 'passwosrd')