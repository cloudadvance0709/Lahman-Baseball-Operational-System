import json

# DFF TODO -- Not critical for W4111, but should switch from print statements to logging framework.
import logging

from datetime import datetime

from flask import Flask, Response
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

import utils.rest_utils as rest_utils
import pymysql
import json

from Services.FantasyService.FantasyTeam import FantasyTeam as FantasyTeam
from Services.FantasyService.FantasyManager import FantasyManager as FantasyManager
from Services.FantasyService.FantasyLeague import FantasyLeague as FantasyLeague
from Services.FantasyService.FantasyPlayer import FantasyPlayer as FantasyPlayer
from Services.LahmanService.PersonService import PersonService as PersonService
from Services.LahmanService.TeamService import TeamService as TeamService
from Services.DataServices.Neo4JDataTable import HW3Graph as HW3Graph


# DFF TODO - We should not hardcode this here, and we should do in a context/environment service.
# OK for W4111 - This is not a course on microservices and robust programming.
#
#

conn = pymysql.connect(
    host = "tutorialdb.c1a7fjnzmzlo.us-east-2.rds.amazonaws.com",
    user = "admin",
    password = "chilee0709",
    database = "HW3_s21",
    cursorclass = pymysql.cursors.DictCursor
)

_service_factory = {
    "fantasy_player": FantasyPlayer({
        "db_name": "HW3_s21",
        "table_name": "fantasy_player",
        "db_connect_info": {
            "user": "admin",
            "password": "chilee0709",
            "host": "tutorialdb.c1a7fjnzmzlo.us-east-2.rds.amazonaws.com",
            "db": "HW3_s21"
        },
        "key_columns": ["playerID"]
    }),
    "fantasy_team": FantasyTeam({
        "db_name": "HW3_s21",
        "table_name": "fantasy_team",
        "db_connect_info": {
            "user": "admin",
            "password": "chilee0709",
            "host": "tutorialdb.c1a7fjnzmzlo.us-east-2.rds.amazonaws.com",
            "db": "HW3_s21"
        },
        "key_columns": ["teamID"]
    }),
    "fantasy_manager": FantasyManager({
        "db_name": "HW3_s21",
        "table_name": "fantasy_manager",
        "db_connect_info": {
            "user": "admin",
            "password": "chilee0709",
            "host": "tutorialdb.c1a7fjnzmzlo.us-east-2.rds.amazonaws.com",
            "db": "HW3_s21"
        },
        "key_columns": ["managerID"]
    }),
    "fantasy_league": FantasyLeague({
        "db_name": "HW3_s21",
        "table_name": "fantasy_league",
        "db_connect_info": {
            "user": "admin",
            "password": "chilee0709",
            "host": "tutorialdb.c1a7fjnzmzlo.us-east-2.rds.amazonaws.com",
            "db": "HW3_s21"
        },
        "key_columns": ["leagueID"]
    }),
    "person": PersonService({
        "db_name": "HW3_s21",
        "table_name": "people",
        "db_connect_info": {
            "user": "admin",
            "password": "chilee0709",
            "host": "tutorialdb.c1a7fjnzmzlo.us-east-2.rds.amazonaws.com",
            "db": "HW3_s21"
        },
        "key_columns": ["playerID"]
    }),
    "teams": TeamService({
        "db_name": "HW3_s21",
        "table_name": "recent_teams",
        "db_connect_info": {
            "user": "admin",
            "password": "chilee0709",
            "host": "tutorialdb.c1a7fjnzmzlo.us-east-2.rds.amazonaws.com",
            "db": "HW3_s21"
        },
        "key_columns": ["teamID", "yearID"]
    })

}


# Given the "resource"
def _get_service_by_name(s_name):
    result = _service_factory.get(s_name, None)
    return result


app = Flask(__name__)
CORS(app)

##################################################################################################################


# DFF TODO A real service would have more robust health check methods.
@app.route("/health", methods=["GET"])
def health_check():
    rsp_data = {"status": "healthy", "time": str(datetime.now())}
    rsp_str = json.dumps(rsp_data)
    rsp = Response(rsp_str, status=200, content_type="app/json")
    return rsp


# TODO Remove later. Solely for explanatory purposes.
# The method take any REST request, and produces a response indicating what
# the parameters, headers, etc. are. This is simply for education purposes.
#
@app.route("/api/demo/<parameter1>", methods=["GET", "POST", "PUT", "DELETE"])
@app.route("/api/demo/", methods=["GET", "POST", "PUT", "DELETE"])
def demo(parameter1=None):

    # Mostly for isolation. The rest of the method is isolated from the specifics of Flask.
    inputs = rest_utils.RESTContext(request, {"parameter1": parameter1})

    # DFF TODO -- We should replace with logging.
    r_json = inputs.to_json()
    msg = {
        "/demo received the following inputs": inputs.to_json()
    }
    print("/api/demo/<parameter> received/returned:\n", msg)

    rsp = Response(json.dumps(msg), status=200, content_type="application/json")
    return rsp


##################################################################################################################
# Actual routes begin here.
#
#

@app.route("/api/<resource>/count", methods=["GET"])
def get_resource_count(resource):
    """
    Currently not implemented. Need to revise.
    """
    rsp = Response("NOT IMPLEMENTED", status=501)
    return rsp

    """
    try:
        # DFF TODO Change this to a DTO/object with properties from a dict.
        inputs = rest_utils.RESTContext(request)
        rest_utils.log_request("get_resource_count", inputs)

        service = _get_service_by_name(resource)

        if service is not None:
            res = service.get_count()
            if res is not None:
                res = {"count": res}
                res = json.dumps(res, default=str)
                rsp = Response(res, status=200, content_type="application/JSON")
            else:
                rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        else:
            rsp = Response("NOT FOUND", status=404)

    except Exception as e:
        # TODO Put a common handler to catch excceptions, log the error and return correct
        # HTTP status code.
        print("/api/" + resource + "/count, e = ", e)
        rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    return rsp
    """


@app.route("/api/people/<player_id>/career_batting", methods=["GET"])
def get_career_batting(player_id):

    rsp = Response("NOT IMPLEMENTED", status=501)
    return rsp

    try:
        # DFF TODO Change this to a DTO/object with properties from a dict.
        inputs = rest_utils.RESTContext(request)
        rest_utils.log_request("get_resource_count", inputs)

        service = _get_service_by_name("player_performance")

        if service is not None:
            if inputs.method == "GET":
                res = service.get_career_batting(player_id)
                if res is not None:
                    res = json.dumps(res, default=str)
                    rsp = Response(res, status=200, content_type="application/JSON")
                else:
                    rsp = Response("NOT FOUND", status=404, content_type="text/plain")
            else:
                rsp = Response("NOT IMPLEMENTED", status=501)
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    except Exception as e:
        # TODO Put a common handler to catch excceptions, log the error and return correct
        # HTTP status code.
        print("/api/players/<player_id>/career_batting, e = ", e)
        rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    return rsp


@app.route("/api/<resource>", methods=["GET", "POST"])
def get_resource_by_query(resource):

    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    try:
        # DFF TODO Change this to a DTO/object with properties from a dict.
        inputs = rest_utils.RESTContext(request)
        rest_utils.log_request("get_resource_by_query", inputs)

        if inputs.method == "GET":

            template = inputs.args
            service = _get_service_by_name(resource)

            if service is not None:
                res = service.find_by_template(template, inputs.fields)
                if res is not None:
                    res = json.dumps(res, default=str)
                    rsp = Response(res, status=200, content_type="application/JSON")
                else:
                    rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        elif inputs.method == "POST":

            service = _get_service_by_name(resource)

            if service is not None:
                res = service.create(inputs.data)
                if res is not None:
                    key = "_".join(res.values())
                    headers = {"location": "/api/" + resource + "/" + key}
                    rsp = Response("CREATED", status=201, content_type="text/plain", headers=headers)
                else:
                    rsp = Response("UNPROCESSABLE ENTITY", status=422, content_type="text/plain")
        else:
            rsp = Response("NOT IMPLEMENTED", status=501)
    except Exception as e:
        # TODO Put a common handler to catch excceptions, log the error and return correct
        # HTTP status code.
        print("/api/<resource>, e = ", e)
        rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    return rsp

"""
@app.route("/api/<resource>/<resource_id>", methods=["GET", "PUT", "DELETE"])
def resource_by_id(resource, resource_id):

    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    try:
        
        inputs = rest_utils.RESTContext(request)
        rest_utils.log_request("resource_by_id", inputs)

        # The resource_id can map to a single attribute, e.g. SSNO
        # Or map to a composite key, e.g. {countrycode, phoneno}
        # We encode this as "countrycode_phoneno"
        resource_key_columns = rest_utils.split_key_string(resource_id)

        if inputs.method == "GET":
            service = _get_service_by_name(resource)

            if service is not None:
                res = service.find_by_primary_key(resource_key_columns, inputs.fields)
                if res is not None:
                    res = json.dumps(res, default=str)
                    rsp = Response(res, status=200, content_type="application/JSON")
                else:
                    rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        elif inputs.method == "PUT":

            service = _get_service_by_name(resource)

            if service is not None:
                res = service.update(resource_key_columns, inputs.data)
                if res is not None:
                    rsp = Response("OK", status=200, content_type="text/plain")
                else:
                    rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        else:
            rsp = Response("NOT IMPLEMENTED", status=501)

    except Exception as e:
        # DFF TODO -- Need to handle integrity exceptions, etc. more clearly, e.g. 422, etc.
        # TODO Put a common handler to catch excceptions, log the error and return correct
        # HTTP status code.
        print("/api/person, e = ", e)
        rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    return rsp
"""

@app.route("/api/people/search/<pattern>", methods=["GET"])
def get_person_by_pattern(pattern):

    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    try:
        # DFF TODO Change this to a DTO/object with properties from a dict.

        inputs = rest_utils.RESTContext(request)
        rest_utils.log_request("get_person_by_pattern", inputs)

        #resource_key_columns = rest_utils.split_key_string(resource_id)

        if inputs.method == "GET":
            service = _get_service_by_name("people")

            if service is not None:
                res = service.get_by_pattern("nameLast", pattern)
                if res is not None:
                    res = json.dumps(res, default=str)
                    rsp = Response(res, status=200, content_type="application/JSON")
                else:
                    rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        else:
            rsp = Response("NOT IMPLEMENTED", status=501)
    except Exception as e:
        # TODO Put a common handler to catch excceptions, log the error and return correct
        # HTTP status code.
        print("/api/people/pattern, e = ", e)
        rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    return rsp


@app.route("/api/FantasyPlayer", methods=["GET", "POST"])
def do_fantasy_player():

    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    try:
        # DFF TODO Change this to a DTO/object with properties from a dict.
        inputs = rest_utils.RESTContext(request)
        rest_utils.log_request("get_resource_by_query", inputs)

        if inputs.method == "GET":

            template = inputs.args
            service = _get_service_by_name("fantasy_player")

            if service is not None:
                res = service.find_by_template(template, inputs.fields)
                if res is not None:
                    res = json.dumps(res, default=str)
                    rsp = Response(res, status=200, content_type="application/JSON")
                else:
                    rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        elif inputs.method == "POST":

            service = _get_service_by_name("fantasy_player")

            if service is not None:
                res = service.create(inputs.data)
                if res is not None:
                    key = "_".join(res.values())
                    headers = {"location": "/api/" + "fantasy_player" + "/" + key}
                    rsp = Response("CREATED", status=201, content_type="text/plain", headers=headers)
                else:
                    rsp = Response("UNPROCESSABLE ENTITY", status=422, content_type="text/plain")
        else:
            rsp = Response("NOT IMPLEMENTED", status=501)
    except Exception as e:
        # TODO Put a common handler to catch excceptions, log the error and return correct
        # HTTP status code.
        print("/api/FantasyPlayer, e = ", e)
        rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    return rsp

@app.route("/api/FantasyTeam", methods=["GET", "POST"])
def do_fantasy_team():

    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    try:
        # DFF TODO Change this to a DTO/object with properties from a dict.
        inputs = rest_utils.RESTContext(request)
        rest_utils.log_request("get_resource_by_query", inputs)

        if inputs.method == "GET":

            template = inputs.args
            service = _get_service_by_name("fantasy_team")

            if service is not None:
                res = service.find_by_template(template, inputs.fields)
                if res is not None:
                    res = json.dumps(res, default=str)
                    rsp = Response(res, status=200, content_type="application/JSON")
                else:
                    rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        elif inputs.method == "POST":

            service = _get_service_by_name("fantasy_team")

            if service is not None:
                res = service.create(inputs.data)
                if res is not None:
                    key = "_".join(res.values())
                    headers = {"location": "/api/" + "fantasy_team" + "/" + key}
                    rsp = Response("CREATED", status=201, content_type="text/plain", headers=headers)
                else:
                    rsp = Response("UNPROCESSABLE ENTITY", status=422, content_type="text/plain")
        else:
            rsp = Response("NOT IMPLEMENTED", status=501)
    except Exception as e:
        # TODO Put a common handler to catch excceptions, log the error and return correct
        # HTTP status code.
        print("/api/FantasyTeam, e = ", e)
        rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    return rsp

@app.route("/api/FantasyTeam/<teamID>", methods=["DELETE"])
def delete_fantasy_team(teamID):
    q = "delete from fantasy_team where teamID=%s";
    cur = conn.cursor()
    cur.execute(q, (teamID))
    res = cur.fetchall()
    conn.commit()
    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/FantasyTeam/<teamID>/FantasyPlayer/<playerID>", methods=["DELETE"])
def delete_fantasy_player_teamID_playerID(teamID, playerID):
    q = "delete from fantasy_player where teamID=%s and playerID=%s";
    cur = conn.cursor()
    cur.execute(q, (teamID, playerID))
    res = cur.fetchall()
    conn.commit()
    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/FantasyManager/<managerID>", methods=["DELETE"])
def delete_fantasy_manager_managerID(managerID):
    q = "delete from fantasy_manager where managerID=%s";
    cur = conn.cursor()
    cur.execute(q, (managerID))
    res = cur.fetchall()
    conn.commit()
    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/FantasyManager/<managerID>/FantasyTeam/<teamID>", methods=["DELETE"])
def delete_fantasy_team_managerID_teamID(managerID, teamID):
    q = "delete from fantasy_team where managerID=%s and teamID=%s";
    cur = conn.cursor()
    cur.execute(q, (managerID, teamID))
    res = cur.fetchall()
    conn.commit()
    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/FantasyManager/<managerID>/FantasyLeague/<leagueID>", methods=["DELETE"])
def delete_fantasy_league_managerID_leagueID(managerID, leagueID):
    q = "delete from fantasy_league where managerID=%s and leagueID=%s";
    cur = conn.cursor()
    cur.execute(q, (managerID, leagueID))
    res = cur.fetchall()
    conn.commit()
    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp



@app.route("/api/FantasyManager", methods=["GET", "POST"])
def do_fantasy_manager():

    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    try:
        # DFF TODO Change this to a DTO/object with properties from a dict.
        inputs = rest_utils.RESTContext(request)
        rest_utils.log_request("get_resource_by_query", inputs)

        if inputs.method == "GET":

            template = inputs.args
            service = _get_service_by_name("fantasy_manager")

            if service is not None:
                res = service.find_by_template(template, inputs.fields)
                if res is not None:
                    res = json.dumps(res, default=str)
                    rsp = Response(res, status=200, content_type="application/JSON")
                else:
                    rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        elif inputs.method == "POST":

            service = _get_service_by_name("fantasy_manager")

            if service is not None:
                res = service.create(inputs.data)
                if res is not None:
                    key = "_".join(res.values())
                    headers = {"location": "/api/" + "fantasy_manager" + "/" + key}
                    rsp = Response("CREATED", status=201, content_type="text/plain", headers=headers)
                else:
                    rsp = Response("UNPROCESSABLE ENTITY", status=422, content_type="text/plain")
        else:
            rsp = Response("NOT IMPLEMENTED", status=501)
    except Exception as e:
        # TODO Put a common handler to catch excceptions, log the error and return correct
        # HTTP status code.
        print("/api/FantasyManager, e = ", e)
        rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    return rsp

@app.route("/api/FantasyLeague", methods=["GET", "POST"])
def do_fantasy_league():

    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    try:
        # DFF TODO Change this to a DTO/object with properties from a dict.
        inputs = rest_utils.RESTContext(request)
        rest_utils.log_request("get_resource_by_query", inputs)

        if inputs.method == "GET":

            template = inputs.args
            service = _get_service_by_name("fantasy_league")

            if service is not None:
                res = service.find_by_template(template, inputs.fields)#------差別
                if res is not None:
                    res = json.dumps(res, default=str)
                    rsp = Response(res, status=200, content_type="application/JSON")
                else:
                    rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        elif inputs.method == "POST":

            service = _get_service_by_name("fantasy_league")

            if service is not None:
                res = service.create(inputs.data)#------差別
                if res is not None:
                    key = "_".join(res.values())
                    headers = {"location": "/api/" + "fantasy_league" + "/" + key}
                    rsp = Response("CREATED", status=201, content_type="text/plain", headers=headers)
                else:
                    rsp = Response("UNPROCESSABLE ENTITY", status=422, content_type="text/plain")
        else:
            rsp = Response("NOT IMPLEMENTED", status=501)
    except Exception as e:
        # TODO Put a common handler to catch excceptions, log the error and return correct
        # HTTP status code.
        print("/api/FantasyLeague, e = ", e)
        rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    return rsp

@app.route("/api/FantasyTeam/<teamID>/FantasyPlayer", methods=["GET"])
def fantasyTeam_fantasyPlayer(teamID):
    q = "select * from fantasy_player where teamID=%s";
    cur = conn.cursor()
    cur.execute(q, (teamID))
    res = cur.fetchall()
    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/FantasyLeague/<leagueID>/FantasyTeam", methods=["GET"])
def fantasyLeague_fantasyTeam(leagueID):
    q = "select * from fantasy_team where leagueID=%s";
    cur = conn.cursor()
    cur.execute(q, (leagueID))
    res = cur.fetchall()
    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/FantasyTeam/<teamID>", methods=["GET"])
def get_fantasy_team_teamID(teamID):
    q = "select * from fantasy_team where teamID=%s";
    cur = conn.cursor()
    cur.execute(q, (teamID))
    res = cur.fetchall()
    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/FantasyTeam/<teamID>/FantasyPlayer/<playerID>", methods=["GET"])
def get_fantasy_player_teamID_playerID(teamID, playerID):
    q = "select * from fantasy_player where teamID=%s and playerID=%s";
    cur = conn.cursor()
    cur.execute(q, (teamID, playerID))
    res = cur.fetchall()
    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/FantasyManager/<managerID>", methods=["GET"])
def get_fantasy_manager_managerID(managerID):
    q = "select * from fantasy_manager where managerID=%s";
    cur = conn.cursor()
    cur.execute(q, (managerID))
    res = cur.fetchall()
    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/FantasyManager/<managerID>/FantasyTeam/<teamID>", methods=["GET"])
def get_fantasy_team_managerID_teamID(managerID, teamID):
    q = "select * from fantasy_team where managerID=%s and teamID=%s";
    cur = conn.cursor()
    cur.execute(q, (managerID, teamID))
    res = cur.fetchall()
    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/FantasyManager/<managerID>/FantasyLeague/<leagueID>", methods=["GET"])
def get_fantasy_league_managerID_leagueID(managerID, leagueID):
    q = "select * from fantasy_league where managerID=%s and leagueID=%s";
    cur = conn.cursor()
    cur.execute(q, (managerID, leagueID))
    res = cur.fetchall()
    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/FantasyTeam/<teamID>", methods=["PUT"])
def put_fantasy_team_teamID(teamID):
    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    try:
        inputs = rest_utils.RESTContext(request)
        rest_utils.log_request("resource_by_id", inputs)

        # The resource_id can map to a single attribute, e.g. SSNO
        # Or map to a composite key, e.g. {countrycode, phoneno}
        # We encode this as "countrycode_phoneno"
        resource_key_columns = rest_utils.split_key_string(teamID)

        if inputs.method == "PUT":

            service = _get_service_by_name("fantasy_team")

            if service is not None:
                res = service.update(resource_key_columns, inputs.data)
                if res is not None:
                    rsp = Response("OK", status=200, content_type="text/plain")
                else:
                    rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        else:
            rsp = Response("NOT IMPLEMENTED", status=501)

    except Exception as e:
        # DFF TODO -- Need to handle integrity exceptions, etc. more clearly, e.g. 422, etc.
        # TODO Put a common handler to catch excceptions, log the error and return correct
        # HTTP status code.
        print("e = ", e)
        rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    return rsp


@app.route("/api/FantasyTeam/<teamID>/FantasyPlayer/<playerID>", methods=["PUT"])
def put_fantasy_player_teamID_playerID(teamID, playerID):
    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    inputs = rest_utils.RESTContext(request)
    dataAll = inputs.data

    if "teamID" in dataAll and "playerID" in dataAll:
        q = "UPDATE fantasy_player SET teamID=%s, playerID=%s where teamID=%s and playerID=%s"
        cur = conn.cursor()
        cur.execute(q, (dataAll["teamID"], dataAll["playerID"], teamID, playerID))
        res = cur.fetchall()
        conn.commit()
    elif "teamID" in dataAll:
        q = "UPDATE fantasy_player SET teamID=%s where teamID=%s and playerID=%s"
        cur = conn.cursor()
        cur.execute(q, (dataAll["teamID"], teamID, playerID))
        res = cur.fetchall()
        conn.commit()
    elif "playerID" in dataAll:
        q = "UPDATE fantasy_player SET playerID=%s where teamID=%s and playerID=%s"
        cur = conn.cursor()
        cur.execute(q, (dataAll["playerID"], teamID, playerID))
        res = cur.fetchall()
        conn.commit()

    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/FantasyManager/<managerID>", methods=["PUT"])
def put_fantasy_manager_managerID(managerID):
    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    try:
        inputs = rest_utils.RESTContext(request)
        rest_utils.log_request("resource_by_id", inputs)

        resource_key_columns = rest_utils.split_key_string(managerID)

        if inputs.method == "PUT":

            service = _get_service_by_name("fantasy_manager")

            if service is not None:
                res = service.update(resource_key_columns, inputs.data)
                if res is not None:
                    rsp = Response("OK", status=200, content_type="text/plain")
                else:
                    rsp = Response("NOT FOUND", status=404, content_type="text/plain")
        else:
            rsp = Response("NOT IMPLEMENTED", status=501)

    except Exception as e:
        # DFF TODO -- Need to handle integrity exceptions, etc. more clearly, e.g. 422, etc.
        # TODO Put a common handler to catch excceptions, log the error and return correct
        # HTTP status code.
        print("e = ", e)
        rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    return rsp


@app.route("/api/FantasyManager/<managerID>/FantasyTeam/<teamID>", methods=["PUT"])
def put_fantasy_team_managerID_teamID(managerID, teamID):
    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    inputs = rest_utils.RESTContext(request)
    dataAll = inputs.data

    if "managerID" in dataAll and "teamID" in dataAll:
        q = "UPDATE fantasy_team SET managerID=%s, teamID=%s where managerID=%s and teamID=%s"
        cur = conn.cursor()
        cur.execute(q, (dataAll["managerID"], dataAll["teamID"], managerID, teamID))
        res = cur.fetchall()
        conn.commit()
    elif "managerID" in dataAll:
        q = "UPDATE fantasy_team SET managerID=%s where managerID=%s and teamID=%s"
        cur = conn.cursor()
        cur.execute(q, (dataAll["managerID"], managerID, teamID))
        res = cur.fetchall()
        conn.commit()
    elif "teamID" in dataAll:
        q = "UPDATE fantasy_team SET teamID=%s where managerID=%s and teamID=%s"
        cur = conn.cursor()
        cur.execute(q, (dataAll["teamID"], managerID, teamID))
        res = cur.fetchall()
        conn.commit()

    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/FantasyManager/<managerID>/FantasyLeague/<leagueID>", methods=["PUT"])
def put_fantasy_league_managerID_leagueID(managerID, leagueID):
    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")

    inputs = rest_utils.RESTContext(request)
    dataAll = inputs.data

    if "managerID" in dataAll and "leagueID" in dataAll:
        q = "UPDATE fantasy_league SET managerID=%s, leagueID=%s where managerID=%s and leagueID=%s"
        cur = conn.cursor()
        cur.execute(q, (dataAll["managerID"], dataAll["leagueID"], managerID, leagueID))
        res = cur.fetchall()
        conn.commit()
    elif "managerID" in dataAll:
        q = "UPDATE fantasy_league SET managerID=%s where managerID=%s and leagueID=%s"
        cur = conn.cursor()
        cur.execute(q, (dataAll["managerID"], managerID, leagueID))
        res = cur.fetchall()
        conn.commit()
    elif "leagueID" in dataAll:
        q = "UPDATE fantasy_league SET leagueID=%s where managerID=%s and leagueID=%s"
        cur = conn.cursor()
        cur.execute(q, (dataAll["leagueID"], managerID, leagueID))
        res = cur.fetchall()
        conn.commit()

    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


@app.route("/api/FantasyTeam/<teamID>/FantasyPlayer", methods=["POST"])
def post_fantasy_player_teamID(teamID):
    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")
    inputs = rest_utils.RESTContext(request)
    dataAll = inputs.data

    if "playerID" in dataAll:
        cur = conn.cursor()
        cur.execute("INSERT INTO fantasy_player(playerID, teamID) VALUES (%s, %s)",
                    (dataAll["playerID"], teamID))
        res = cur.fetchall()
        conn.commit()

    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

@app.route("/api/FantasyLeague/<leagueID>/FantasyTeam", methods=["POST"])
def post_fantasy_team_leagueID(leagueID):
    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")
    inputs = rest_utils.RESTContext(request)
    dataAll = inputs.data

    if "teamID" in dataAll and "teamName" in dataAll and "created" in dataAll and "managerID" in dataAll:
        cur = conn.cursor()
        cur.execute("INSERT INTO fantasy_team(teamID, teamName, leagueID, created, managerID) VALUES (%s, %s, %s, %s, %s)",
                    (dataAll["teamID"], dataAll["teamName"], leagueID ,dataAll["created"], dataAll["managerID"]))
        res = cur.fetchall()
        conn.commit()

    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp


def t1():
    hw3g = HW3Graph() #connect to neo4j database

def t2(): #match
    q = "match (n:Person {name: 'Tom Hanks'}) return n"
    hw3g = HW3Graph()
    res = hw3g.run_q(q, args=None)
    print("t2 -- res =", res)

    tmp = { "label": "Person", "template": {"name": "Tom Hanks"}}
    res2 = hw3g.find_nodes_by_template(tmp)
    print("t2 -- res =", res2)

def t3(): # create node

    hw3g = HW3Graph()
    res = hw3g.create_node(label="Person", name="Fred Astaire", nconst='nm0000001', firstName='Fred',
                     lastName='Astaire')
    print("t3 -- res = ", res)

"""
@app.route("/api/FantasyManager/<managerID>/Follows", methods=["GET"])
def get_follows_managerID():
"""

@app.route("/api/FantasyManager/<managerID>/Follows", methods=["GET"])
def t5(managerID):
    q3 = "MATCH (a)-[r:FOLLOWS]->(b) WHERE a.managerID = '" + managerID +"' RETURN a"
    hw3g = HW3Graph()
    res = hw3g.run_q(q3, args=None)
    print(res)

    if res is not None:
        for r in res:
            res = json.dumps(r, default=str)
            rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/FantasyManager/<managerID>/Likes", methods=["GET"])
def t6(managerID):
    print(type(managerID))
    q3 = "MATCH (a)-[r:LIKES]->(b) WHERE a.managerID = '" + managerID +"' RETURN a"
    hw3g = HW3Graph()
    res = hw3g.run_q(q3, args=None)
    print(res)

    if res is not None:
        for r in res:
            res = json.dumps(r, default=str)
            rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/FantasyManager/<managerID>/Follows", methods=["POST"])
def t8(managerID):
    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")
    inputs = rest_utils.RESTContext(request)
    dataAll = inputs.data

    q3 = "MATCH (n:FantasyManager{managerID:'" + managerID + "'}), (c:FantasyPlayer{playerID:'" + dataAll["playerID"] + "'}) create (n)-[r:FOLLOWS]->(c)"
    hw3g = HW3Graph()
    res = hw3g.run_q(q3, args=None)

    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/FantasyManager/<managerID>/Likes", methods=["POST"])
def t10(managerID):
    rsp = Response("INTERNAL ERROR", status=500, content_type="text/plain")
    inputs = rest_utils.RESTContext(request)
    dataAll = inputs.data

    q3 = "MATCH (n:FantasyManager{managerID:'" + managerID + "'}), (c:FantasyTeam{teamID:'" + dataAll["teamID"] + "'}) create (n)-[r:LIKES]->(c)"
    hw3g = HW3Graph()
    res = hw3g.run_q(q3, args=None)

    if res is not None:
        res = json.dumps(res, default=str)
        rsp = Response(res, status=200, content_type="application/JSON")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == '__main__':
    #host, port = ctx.get_host_and_port()

    # DFF TODO We will handle host and SSL certs different in deployments.
    app.run(host="0.0.0.0", port=5001)

