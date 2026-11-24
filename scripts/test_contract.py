import copy, hashlib, json, tempfile, unittest
from pathlib import Path
from check_contract import inspect_plan

class ContractTests(unittest.TestCase):
    def plan(self):
        return json.loads((Path(__file__).resolve().parents[1]/'examples/contract.json').read_text(encoding='utf-8'))
    def test_valid_example_is_not_modified(self):
        d=self.plan();before=copy.deepcopy(d)
        self.assertTrue(inspect_plan(d)['contract_valid'])
        self.assertEqual(d,before)
    def test_foreign_role_and_malformed_input_are_rejected(self):
        d=self.plan();d['skill']='foreign-skill'
        self.assertFalse(inspect_plan(d)['contract_valid'])
        for bad in [None,[],{},'text',{'skill':self.plan()['skill']}]:
            self.assertFalse(inspect_plan(bad)['contract_valid'])

    def test_original_audio_selection_and_unverified_lyrics(self):
        d=self.plan();d['audio_out']=31
        self.assertFalse(inspect_plan(d)['contract_valid'])
        d=self.plan();d['lyrics_status']='unverified';d['lyric_cues']=[{'start':1,'end':5,'text':'guessed lyric'}]
        self.assertFalse(inspect_plan(d)['contract_valid'])
    def test_instrumental_is_valid_and_rate_change_requires_choice(self):
        d=self.plan();self.assertTrue(inspect_plan(d)['contract_valid'])
        d['audio_rate']=2;d['output_duration']=10;d['shots']=[{'start':0,'end':10,'visual_anchor':'consistent scene'}];d['beats']=[0,5]
        self.assertFalse(inspect_plan(d)['contract_valid'])
        d['audio_rate_approved']=True
        self.assertTrue(inspect_plan(d)['contract_valid'])


if __name__=='__main__': unittest.main()
