from core.resources.base import BaseResource
from flask import request
from core.utils.data_api import AccessToUsers
from core.controllers.controllers import LoginController, SessionDetailsController


class Login(BaseResource):

    def post(self):
        data, errors = self.login_schema.load(request.get_json())
        if errors and not data:
            return 'wrong input data, please try again', 400
        user_id = AccessToUsers.post(data['username'], data['password'])
        login_controller = LoginController()
        return login_controller.login(user_id)


class SessionDetails(BaseResource):

    def get(self):
        data, errors = self.session_id_schema.load(request.get_json())
        if errors and not data:
            return 'wrong data', 400
        sid = data['sid']
        session_details_controller = SessionDetailsController()
        return session_details_controller.get_details(sid)
