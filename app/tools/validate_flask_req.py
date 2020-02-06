import flask

from app.tools.method_response import MethodResponse


def validate_post_req(fl_request: flask.request, params_list: list = None):
    """
        Checking payload of a Flask POST request
        :param  fl_request:     payload to be validate
        :param  params_list:    list of params that are required to be in payload
        :return:                [False, message text] in case it fails. [True, list_of_params_values] in case it is OK
        """
    result_payload = __validate_flask_payload(fl_request)
    if result_payload.success:
        return validate_params(payload=result_payload.data, params_list=params_list)


def __validate_flask_payload(req_val: flask.request):
    """
        Sub method of helper.validate_post_req. Just checking if request holds a json payload
        :param  req_val:     payload to be validated
        :return:             [False, message text] in case it fails. [json_payload] in case it is OK
        """
    if not req_val.data or not req_val.get_json(silent=True):
        return MethodResponse(message="NO Json in payload")
    req_content = req_val.json
    if not req_content or type(req_content) != dict:
        return MethodResponse(message='Paylaod not formatted properly')
    return MethodResponse(success=True, data=req_content)


def validate_params(payload: dict, params_list: list= None):
    """
       Sub method of helper.validate_post_req. Just checking if param_name or params_list are in the json
       :param  payload:        payload to be validated
       :param  params_list:    list of params that are required to be in payload
       :return:                [False, message text] in case it fails. [True, [list_of_params_values]] in case it is OK
       """
    output_values = []
    for param in params_list:
        if param not in payload or not payload[param]:
            return MethodResponse(message='Parameter: "{}" missing/empty in payload'.format(param))
        output_values.append(payload[param])
    return MethodResponse(success=True, data=output_values)