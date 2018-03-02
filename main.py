# system imports
import time

# aws imports
import boto3

# local imports
from scrape import *
from dynamo_db_utils import *

dynamodb = boto3.resource('dynamodb')

def hs_biology():
    biology_url = "https://quizlet.com/138817444/high-school-science-bowl-biology-flash-cards/"
    create_table('hs_biology')
    time.sleep(60)
    data = scrape_data_evenq_odda(biology_url)
    populate_table(data, table=dynamodb.Table('hs_biology'))

def hs_energy():
    energy_url = "https://quizlet.com/142680213/high-school-science-bowl-energy-flash-cards/"
    create_table('hs_energy')
    time.sleep(60)
    data = scrape_data_evenq_odda(energy_url)
    populate_table(data, table=dynamodb.Table('hs_energy'))

def hs_chemistry():
    chemistry_url = "https://quizlet.com/139906669/high-school-science-bowl-chemistry-flash-cards/"
    create_table('hs_chemistry')
    time.sleep(60)
    data = scrape_data_evenq_odda(chemistry_url)
    populate_table(data, table=dynamodb.Table('hs_chemistry'))

def hs_earth_science():
    earth_science_url = "https://quizlet.com/176482428/high-school-science-bowl-earth-science-flash-cards/"
    create_table('hs_earth_science')
    time.sleep(60)
    data = scrape_data_oddq_evena(earth_science_url)
    populate_table(data, table=dynamodb.Table('hs_earth_science'))

def hs_physics():
    physics_url = "https://quizlet.com/161684083/high-school-science-bowl-physics-flash-cards/"
    create_table('hs_physics')
    time.sleep(60)
    data = scrape_data_oddq_evena(physics_url)
    populate_table(data, table=dynamodb.Table('hs_earth_science'))

def ms_questions():
    url = "https://quizlet.com/183381446/doe-middle-school-science-bowl-sample-questions-flash-cards/"
    create_table('ms_questions')
    time.sleep(60)
    data = scrape_data_oddq_evena(url)
    populate_table(data, table=dynamodb.Table('ms_questions'))

def main():
    hs_biology()
    hs_energy()
    hs_chemistry()
    hs_earth_science()
    hs_physics()
    ms_questions()

if __name__=="__main__":
    main()
