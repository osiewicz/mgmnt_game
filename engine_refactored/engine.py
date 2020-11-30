import random
import itertools

from django.conf import settings
from . import models
from collections import namedtuple

Project = namedtuple('Project', 'cost payoff risk')

# seed -> list of N projects
def game_to_projects(seed):
    wallet_count = settings.PROJECT_COUNT
    generator = random.Random(seed)
    ret = []
    risk_min, risk_max = settings.MIN_RISK, settings.MAX_RISK
    cost_min, cost_max = settings.MIN_COST, settings.MAX_COST
    payoff_min, payoff_max = settings.MIN_PAYOFF, settings.MAX_PAYOFF
    assert payoff_min <= payoff_max
    assert cost_min <= cost_max
    assert risk_min <= risk_max
    assert risk_min >= 0
    assert risk_max <= 1.0
    assert cost_min > 0
    assert payoff_min >= 0
    for _ in range(wallet_count):
        risk = generator.uniform(risk_min, risk_max)
        cost = generator.randint(cost_min, cost_max)
        payoff = generator.randint(payoff_min, payoff_max)
        ret.append(Project(cost, payoff, risk))

    return ret

# list of N projects -> list of lists of possible choices (0-based indices)
def projects_to_wallets(project_count):
    return list(itertools.combinations(range(project_count), settings.WALLET_SIZE))
    
def projects_to_ratings(projects, seed):
    generator = random.Random(seed)
    def rate_project(project):
        # tofix, take risk into account.
        return project.payoff

    return list(map(rate_project, projects))
    
def rate_wallet(project_ratings, wallet):
    return list(map(lambda wallet: sum([project_ratings[i] for i in wallet]), wallets))

