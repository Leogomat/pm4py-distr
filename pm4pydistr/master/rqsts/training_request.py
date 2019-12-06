from pm4pydistr.master.rqsts.basic_request import BasicMasterRequest
from pm4pydistr.configuration import KEYPHRASE
import requests
import json

class TrainingRequest(BasicMasterRequest):
    def __init__(self, session, target_host, target_port, use_transition, no_samples, process):
        self.session = session
        self.target_host = target_host
        self.target_port = target_port
        self.use_transition = use_transition
        self.no_samples = no_samples
        self.process = process
        BasicMasterRequest.__init__(self, None, target_host, target_port, use_transition, no_samples, process)

    def run(self):
        uri = "http://" + self.target_host + ":" + self.target_port + "/doTraining?keyphrase=" + KEYPHRASE + "&process=" + str(
            self.process)

        r = requests.get(uri)
        self.content = json.loads(r.text)