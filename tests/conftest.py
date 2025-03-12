"""
Config file for tests
"""

import pytest

from codeforces_api.types import User, Party, Problem, Member, BlogEntry, Comment


def pytest_addoption(parser):
    parser.addoption(
        "--api_key",
        action="store",
        default="",
        help="API key for tests",
    )
    parser.addoption(
        "--api_secret",
        action="store",
        default="",
        help="API secret for tests",
    )


@pytest.fixture
def api_key(request):
    try:
        import conf

        return conf.api_key
    except ModuleNotFoundError:
        return request.config.getoption("--api_key")


@pytest.fixture
def api_secret(request):
    try:
        import conf

        return conf.api_secret
    except ModuleNotFoundError:
        return request.config.getoption("--api_secret")


@pytest.fixture
def check_user():
    def check(user):
        if isinstance(user, User):
            assert user.email is None or isinstance(user.email, str)
            assert user.open_id is None or isinstance(user.open_id, str)
            assert user.first_name is None or isinstance(user.first_name, str)
            assert user.last_name is None or isinstance(user.last_name, str)
            assert user.country is None or isinstance(user.country, str)
            assert user.vk_id is None or isinstance(user.vk_id, str)
            assert user.country is None or isinstance(user.country, str)
            assert user.city is None or isinstance(user.city, str)
            assert user.organization is None or isinstance(user.organization, str)
            assert isinstance(user.contribution, int)
            assert user.rank is None or isinstance(user.rank, str)
            assert user.rating is None or isinstance(user.rating, int)
            assert user.max_rank is None or isinstance(user.max_rank, str)
            assert user.max_rating is None or isinstance(user.max_rating, int)
            assert isinstance(user.last_online, int)
            assert isinstance(user.registration_time_seconds, int)
            assert isinstance(user.friend_of_count, int)
            assert isinstance(user.avatar, str)
            assert isinstance(user.title_photo, str)
        else:
            assert "email" not in user.keys() or isinstance(user["email"], str)
            assert "openId" not in user.keys() or isinstance(user["openId"], str)
            assert "firstName" not in user.keys() or isinstance(user["firstName"], str)
            assert "lastName" not in user.keys() or isinstance(user["lastName"], str)
            assert "country" not in user.keys() or isinstance(user["country"], str)
            assert "vkId" not in user.keys() or isinstance(user["vkId"], str)
            assert "country" not in user.keys() or isinstance(user["country"], str)
            assert "city" not in user.keys() or isinstance(user["city"], str)
            assert "organization" not in user.keys() or isinstance(user["organization"], str)
            assert isinstance(user["contribution"], int)
            assert "rank" not in user.keys() or isinstance(user["rank"], str)
            assert "rating" not in user.keys() or isinstance(user["rating"], int)
            assert "maxRank" not in user.keys() or isinstance(user["maxRank"], str)
            assert "maxRating" not in user.keys() or isinstance(user["maxRating"], int)
            assert isinstance(user["lastOnlineTimeSeconds"], int)
            assert isinstance(user["registrationTimeSeconds"], int)
            assert isinstance(user["friendOfCount"], int)
            assert isinstance(user["avatar"], str)
            assert isinstance(user["titlePhoto"], str)

    return check


@pytest.fixture
def check_member():
    def check(member):
        if isinstance(member, Member):
            assert isinstance(member.handle, str)
            # assert member.name is None or isinstance(member.name, str)
        else:
            assert isinstance(member["handle"], str)
            assert "name" not in member.keys() or isinstance(member["name"], str)
            pass
    return check


@pytest.fixture
def check_party(check_member):
    def check(party):
        if isinstance(party, Party):
            assert party.contest_id is None or isinstance(party.contest_id, int)
            for member in party.members:
                check_member(member)
            assert party.participant_type in (
                "CONTESTANT", "PRACTICE", "VIRTUAL", "MANAGER", "OUT_OF_COMPETITION"
            )
            assert party.team_id is None or isinstance(party.team_id, int)
            # assert party.team_name is None or isinstance(party.team_name, str)
            assert isinstance(party.ghost, bool)
            assert party.room is None or isinstance(party.room, int)
            assert party.start_time_seconds is None or isinstance(party.start_time_seconds, int)
        else:
            assert "contestId" not in party.keys() or isinstance(party["contestId"], int)
            for member in party["members"]:
                check_member(member)
            assert party["participantType"] in (
                "CONTESTANT", "PRACTICE", "VIRTUAL", "MANAGER", "OUT_OF_COMPETITION"
            )
            assert "teamId" not in party.keys() or isinstance(party["teamId"], int)
            assert "teamName" not in party.keys() or isinstance(party["teamName"], str)
            assert isinstance(party["ghost"], bool)
            assert "room" not in party.keys() or isinstance(party["room"], int)
            assert "startTimeSeconds" not in party.keys() or isinstance(party["startTimeSeconds"], int)

    return check


@pytest.fixture
def check_problem():
    def check(problem):
        if isinstance(problem, Problem):
            assert problem.contest_id is None or isinstance(problem.contest_id, int)
            assert problem.problemset_name is None or isinstance(problem.problemset_name, str)
            assert isinstance(problem.index, str)
            assert isinstance(problem.name, str)
            assert problem.problem_type is None or problem.problem_type in ("PROGRAMMING", "QUESTION")
            assert problem.points is None or isinstance(problem.points, float)
            assert problem.rating is None or isinstance(problem.rating, int)
            assert isinstance(problem.tags, list)
            pass
        else:
            assert "contestId" not in problem.keys() or isinstance(problem["contestId"], int)
            assert "problemsetName" not in problem.keys() or isinstance(problem["problemsetName"], str)
            assert isinstance(problem["index"], str)
            assert isinstance(problem["name"], str)
            assert problem["type"] in ("PROGRAMMING", "QUESTION")
            assert "points" not in problem.keys() or isinstance(problem["points"], float)
            assert "rating" not in problem.keys() or isinstance(problem["rating"], int)
            assert isinstance(problem["tags"], list)

    return check


@pytest.fixture
def check_blog_entry():
    def check(blog_entry):
        if isinstance(blog_entry, BlogEntry):
            assert isinstance(blog_entry.id, int)
            assert isinstance(blog_entry.original_locale, str)
            assert isinstance(blog_entry.creation_time_seconds, int)
            assert isinstance(blog_entry.author_handle, str)
            assert isinstance(blog_entry.title, str)
            assert blog_entry.content is None or isinstance(blog_entry.content, str)
            assert isinstance(blog_entry.locale, str)
            assert isinstance(blog_entry.modification_time_seconds, int)
            assert isinstance(blog_entry.allow_view_history, bool)
            assert isinstance(blog_entry.tags, list)
            assert isinstance(blog_entry.rating, int)
        else:
            assert isinstance(blog_entry["id"], int)
            assert isinstance(blog_entry["originalLocale"], str)
            assert isinstance(blog_entry["creationTimeSeconds"], int)
            assert isinstance(blog_entry["authorHandle"], str)
            assert isinstance(blog_entry["title"], str)
            assert "content" not in blog_entry.keys() or isinstance(blog_entry["content"], str)
            assert isinstance(blog_entry["locale"], str)
            assert isinstance(blog_entry["modificationTimeSeconds"], int)
            assert isinstance(blog_entry["allowViewHistory"], bool)
            assert isinstance(blog_entry["tags"], list)
            assert isinstance(blog_entry["rating"], int)

    return check


@pytest.fixture
def check_comment():
    def check(comment):
        if isinstance(comment, Comment):
            assert isinstance(comment.id, int)
            assert isinstance(comment.creation_time_seconds, int)
            assert isinstance(comment.commentator_handle, str)
            assert isinstance(comment.locale, str)
            assert isinstance(comment.text, str)
            assert comment.parent_comment_id is None or isinstance(comment.parent_comment_id, int)
            assert isinstance(comment.rating, int)
        else:
            assert isinstance(comment["id"], int)
            assert isinstance(comment["creationTimeSeconds"], int)
            assert isinstance(comment["commentatorHandle"], str)
            assert isinstance(comment["locale"], str)
            assert isinstance(comment["text"], str)
            assert "parentCommentId" not in comment.keys() or isinstance(comment["parentCommentId"], int)
            assert isinstance(comment["rating"], int)

    return check
