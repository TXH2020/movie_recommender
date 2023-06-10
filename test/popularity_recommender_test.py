import os
import sys

# add your project directory to the sys.path
project_home = os.getcwd()
if project_home not in sys.path:
    sys.path.insert(0, project_home)
os.chdir(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'prs_project.settings'

import django

django.setup()


from recs.popularity_recommender import PopularityBasedRecs

import unittest


class TestNeighborhoodBasedRecs(unittest.TestCase):

    def test_top_n(self):
        rec_sys = PopularityBasedRecs()

        recs = rec_sys.recommend_items(10)
        self.assertIsNotNone(recs)

    def test_rating_prediction(self):
        rec_sys = PopularityBasedRecs()

        predicted_rating = rec_sys.predict_score(10, '4500214')
        self.assertTrue(predicted_rating > 0)

if __name__ == '__main__':
    unittest.main()
