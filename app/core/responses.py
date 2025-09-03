from flask import jsonify, Response

def success_response(data=None, message="OK", status_code=200):
    """Generate a standardized success response."""

    if status_code == 204:
        return Response(status=204)

    payload = {
        "status": "success",
        "message": message
    }
    if data is not None:
        payload["data"] = data
    return jsonify(payload), status_code

def error_response(message="Error", status_code=400, errors=None):
    """Generate a standardized error response."""

    payload = {
        "status": "error",
        "message": message
    }
    if errors:
        payload["errors"] = errors 
    return jsonify(payload), status_code