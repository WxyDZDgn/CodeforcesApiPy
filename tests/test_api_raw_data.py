"""
Testing requests to api in raw data.
"""

from codeforces_api import CodeforcesApi
import json


def test_blog_entry_comments():
    api = CodeforcesApi(raw_data=True)
    comments = api.blog_entry_comments(74291)
    assert json.dumps(comments)
    for comment in comments:
        if comment["id"] == 584151:
            assert comment["creationTimeSeconds"] == 1582795345


def test_blog_entry_view():
    api = CodeforcesApi(raw_data=True)
    blog_entry = api.blog_entry_view(74291)
    assert json.dumps(blog_entry)
    assert blog_entry["authorHandle"] == "VadVergasov"
    assert blog_entry["originalLocale"] == "ru"
    assert blog_entry["id"] == 74291
    assert blog_entry["title"] == "<p>Codeforces API python</p>"
    assert blog_entry["allowViewHistory"]
    assert blog_entry["tags"] == [
        "#api",
        "api",
        "#codeforces",
        "#python",
        "#python 3",
        "python 3",
    ]
    assert "content" not in blog_entry.keys()


def test_contest_hacks():
    api = CodeforcesApi(raw_data=True)
    hacks = api.contest_hacks(1311)
    assert json.dumps(hacks)
    for hack in hacks:
        if hack["id"] == 615666:
            assert hack["creationTimeSeconds"] == 1582562199
            assert hack["verdict"] == "INVALID_INPUT"
            assert hack["judgeProtocol"] == {
                "protocol": "Validator 'validator.exe' returns exit code 3 [FAIL Integer parameter [name=t] equals to 1000, violates the range [1, 100] (stdin, line 1)]",
                "manual": "false",
                "verdict": "Invalid input",
            }
            assert hack["hacker"]["participantType"] == "PRACTICE"
            assert not hack["hacker"]["ghost"]
            assert hack["hacker"]["members"][0]["handle"] == "VietCT"
            assert "teamId" not in hack["hacker"].keys()
            assert hack["hacker"]["contestId"] == 1311
            assert "room" not in hack["hacker"].keys()
            assert hack["hacker"]["startTimeSeconds"] == 1582554900
            assert hack["defender"]["members"][0]["handle"] == "UMR"
            assert hack["defender"]["participantType"] == "OUT_OF_COMPETITION"
            assert not hack["defender"]["ghost"]
            assert "teamId" not in hack["defender"].keys()
            assert hack["defender"]["contestId"] == 1311
            assert "room" not in hack["defender"].keys()
            assert hack["defender"]["startTimeSeconds"] == 1582554900
            assert hack["problem"]["index"] == "D"
            assert hack["problem"]["name"] == "Three Integers"
            assert hack["problem"]["type"] == "PROGRAMMING"
            assert hack["problem"]["contestId"] == 1311
            assert "problemsetName" not in hack["problem"].keys()
            assert "points" not in hack["problem"].keys()
            assert hack["problem"]["rating"] == 2000
            assert hack["problem"]["tags"] == ["brute force", "math"]
            assert "test" not in hack.keys()
            break


def test_contest_list():
    api = CodeforcesApi(raw_data=True)
    contests = api.contest_list()
    assert json.dumps(contests)
    for contest in contests:
        if contest["id"] == 1496:
            assert contest["name"] == "Codeforces Round 706 (Div. 2)"
            assert contest["type"] == "CF"
            assert contest["phase"] == "FINISHED"
            assert not contest["frozen"]
            assert contest["durationSeconds"] == 7200
            assert contest["startTimeSeconds"] == 1615377900
            assert "preparedBy" not in contest.keys()
            assert "websiteUrl" not in contest.keys()
            assert "description" not in contest.keys()
            assert "difficulty" not in contest.keys()
            assert "kind" not in contest.keys()
            assert "icpcRegion" not in contest.keys()
            assert "country" not in contest.keys()
            assert "city" not in contest.keys()
            assert "season" not in contest.keys()
            break


def test_contest_rating_changes():
    api = CodeforcesApi(raw_data=True)
    changes = api.contest_rating_changes(1313)
    assert json.dumps(changes)
    for change in changes:
        if change["handle"] == "VadVergasov":
            assert change["contestId"] == 1313
            assert change["contestName"] == "Codeforces Round 622 (Div. 2)"
            assert change["rank"] == 2303
            assert change["ratingUpdateTimeSeconds"] == 1582455900
            assert change["oldRating"] == 1330
            assert change["newRating"] == 1381
            break


def test_contest_standings():
    api = CodeforcesApi(raw_data=True)
    standings = api.contest_standings(1313, handles=["VadVergasov"])
    assert json.dumps(standings)
    assert standings["contest"]["id"] == 1313
    assert standings["contest"]["name"] == "Codeforces Round 622 (Div. 2)"
    assert standings["contest"]["type"] == "CF"
    assert standings["contest"]["phase"] == "FINISHED"
    assert not standings["contest"]["frozen"]
    assert standings["contest"]["durationSeconds"] == 7200
    assert standings["contest"]["startTimeSeconds"] == 1582448700
    assert "preparedBy" not in standings["contest"].keys()
    assert "websiteUrl" not in standings["contest"].keys()
    assert "description" not in standings["contest"].keys()
    assert "difficulty" not in standings["contest"].keys()
    assert "kind" not in standings["contest"].keys()
    assert "icpcRegion" not in standings["contest"].keys()
    assert "country" not in standings["contest"].keys()
    assert "city" not in standings["contest"].keys()
    assert "season" not in standings["contest"].keys()
    for problem in standings["problems"]:
        if problem["index"] == "A":
            assert problem["name"] == "Fast Food Restaurant"
            assert problem["type"] == "PROGRAMMING"
            assert problem["contestId"] == 1313
            assert "problemsetName" not in problem.keys()
            assert problem["points"] == 500.0
            assert problem["rating"] == 900
            assert problem["tags"] == ["brute force", "greedy", "implementation"]
            break
    for row in standings["rows"]:
        if row["party"]["members"][0]["handle"] == "VadVergasov":
            assert row["rank"] == 2303
            assert row["party"]["participantType"] == "CONTESTANT"
            assert not row["party"]["ghost"]
            assert "teamId" not in row["party"].keys()
            assert row["party"]["contestId"] == 1313
            assert row["party"]["room"] == 10
            assert row["party"]["startTimeSeconds"] == 1582448700
            assert row["points"] == 1124.0
            assert row["penalty"] == 0
            assert row["successfulHackCount"] == 0
            assert row["unsuccessfulHackCount"] == 0
            for problem in [0, 1, 3, 4, 5]:
                assert "penalty" not in row["problemResults"][problem].keys()
                assert row["problemResults"][problem]["type"] == "FINAL"
                assert row["problemResults"][problem]["rejectedAttemptCount"] == 0
            assert "lastSubmissionTimeSeconds" not in row.keys()
            assert row["problemResults"][0]["points"] == 452.0
            assert row["problemResults"][0]["bestSubmissionTimeSeconds"] == 1466
            assert row["problemResults"][2]["points"] == 672.0
            assert row["problemResults"][2]["rejectedAttemptCount"] == 2
            assert row["problemResults"][2]["bestSubmissionTimeSeconds"] == 3439
            for problem in [1, 3, 4, 5]:
                assert row["problemResults"][problem]["points"] == 0.0
                assert "bestSubmissionTimeSeconds" not in row["problemResults"][problem].keys()
            assert "lastSubmissionTimeSeconds" not in row.keys()
            break


def test_contest_status():
    api = CodeforcesApi(raw_data=True)
    status = api.contest_status(1313)
    assert json.dumps(status)
    for row in status:
        if row["id"] == 71660372:
            assert row["creationTimeSeconds"] == 1582450166
            assert row["relativeTimeSeconds"] == 1466
            assert row["problem"]["index"] == "A"
            assert row["problem"]["name"] == "Fast Food Restaurant"
            assert row["problem"]["type"] == "PROGRAMMING"
            assert row["problem"]["contestId"] == 1313
            assert row["problem"]["points"] == 500.0
            assert row["problem"]["rating"] == 900
            assert row["problem"]["tags"] == ["brute force", "greedy", "implementation"]
            assert row["author"]["members"][0]["handle"] == "VadVergasov"
            assert row["author"]["participantType"] == "CONTESTANT"
            assert not row["author"]["ghost"]
            assert "teamId" not in row["author"].keys()
            assert row["author"]["contestId"] == 1313
            assert row["author"]["room"] == 10
            assert row["author"]["startTimeSeconds"] == 1582448700
            assert row["programmingLanguage"] == "C++17 (GCC 7-32)"
            assert row["testset"] == "TESTS"
            assert row["passedTestCount"] == 5
            assert row["timeConsumedMillis"] == 171
            assert row["memoryConsumedBytes"] == 0
            assert row["contestId"] == 1313
            assert row["verdict"] == "OK"
            assert "points" not in row.keys()


def test_problemset_problems():
    api = CodeforcesApi(raw_data=True)
    problemset = api.problemset_problems()
    assert json.dumps(problemset)
    for problem in problemset["problems"]:
        if problem["name"] == "Single Push":
            assert problem["index"] == "A"
            assert problem["type"] == "PROGRAMMING"
            assert problem["contestId"] == 1253
            assert "problemset_name" not in problem.keys()
            assert problem["points"] == 500.0
            assert problem["rating"] == 1000
            assert problem["tags"] == ["implementation"]
    for statistic in problemset["problem_statistics"]:
        assert isinstance(statistic["index"], str)
        assert isinstance(statistic["solvedCount"], int)
        assert isinstance(statistic["contestId"], int)


def test_recent_status(check_problem, check_party):
    api = CodeforcesApi(raw_data=True)
    status = api.problemset_recent_status(1)[0]
    assert json.dumps(status)
    assert isinstance(status["id"], int)
    assert isinstance(status["creationTimeSeconds"], int)
    assert isinstance(status["relativeTimeSeconds"], int)
    check_problem(status["problem"])
    check_party(status["author"])
    assert isinstance(status["programmingLanguage"], str)
    assert isinstance(status["testset"], str)
    assert isinstance(status["passedTestCount"], int)
    assert isinstance(status["timeConsumedMillis"], int)
    assert isinstance(status["memoryConsumedBytes"], int)
    assert isinstance(status["contestId"], int)
    assert "verdict" not in status.keys() or isinstance(status["verdict"], str)
    assert "points" not in status.keys() or isinstance(status["points"], float)


def test_recent_actions(check_blog_entry, check_comment):
    api = CodeforcesApi(raw_data=True)
    action = api.recent_actions()[0]
    assert json.dumps(action)
    assert isinstance(action["timeSeconds"], int)
    if "blogEntry" in action.keys():
        check_blog_entry(action["blogEntry"])
    if "comment" in action.keys():
        check_comment(action["comment"])


def test_user_blog_entries():
    api = CodeforcesApi(raw_data=True)
    entries = api.user_blog_entries("VadVergasov")
    assert json.dumps(entries)
    for entry in entries:
        if entry["id"] == 74291:
            assert entry["authorHandle"] == "VadVergasov"
            assert entry["originalLocale"] == "ru"
            assert entry["id"] == 74291
            assert entry["title"] == "<p>Codeforces API python</p>"
            assert entry["allowViewHistory"]
            assert entry["tags"] == [
                "#api",
                "api",
                "#codeforces",
                "#python",
                "#python 3",
                "python 3",
            ]
            assert "content" not in entry.keys()


def test_user_info(check_user):
    api = CodeforcesApi(raw_data=True)
    info = api.user_info(["VadVergasov", "tourist"])
    assert json.dumps(info)
    for user in info:
        check_user(user)


def test_user_rated_list(check_user):
    api = CodeforcesApi(raw_data=True)
    users = api.user_rated_list(True)
    assert json.dumps(users)
    for user in users:
        check_user(user)


def test_user_rating():
    api = CodeforcesApi(raw_data=True)
    ratings = api.user_rating("VadVergasov")
    assert json.dumps(ratings)
    for rating in ratings:
        assert isinstance(rating["contestId"], int)
        assert isinstance(rating["contestName"], str)
        assert isinstance(rating["handle"], str)
        assert isinstance(rating["rank"], int)
        assert isinstance(rating["ratingUpdateTimeSeconds"], int)
        assert isinstance(rating["oldRating"], int)
        assert isinstance(rating["newRating"], int)


def test_user_status(check_problem, check_party):
    api = CodeforcesApi(raw_data=True)
    status = api.user_status("VadVergasov")
    assert json.dumps(status)
    for row in status:
        assert isinstance(row["id"], int)
        assert isinstance(row["creationTimeSeconds"], int)
        assert isinstance(row["relativeTimeSeconds"], int)
        check_problem(row["problem"])
        check_party(row["author"])
        assert isinstance(row["programmingLanguage"], str)
        assert isinstance(row["testset"], str)
        assert isinstance(row["passedTestCount"], int)
        assert isinstance(row["timeConsumedMillis"], int)
        assert isinstance(row["memoryConsumedBytes"], int)
        assert "contestId" not in row.keys() or isinstance(row["contestId"], int)
        assert "verdict" not in row.keys() or isinstance(row["verdict"], str)
        assert "points" not in row.keys() or isinstance(row["points"], float)
