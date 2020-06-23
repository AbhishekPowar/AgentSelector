from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from agents.models import Agents
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def agent(request):
    return render(request, 'agent.html', {})


def customer(request):
    return render(request, 'customer.html', {})


def customerReg(request):
    from random import choice
    mode = request.GET.get('Mode', 'random')
    roles = request.GET.get('roles', None)
    roles = ' '.join(sorted(roles.split('-')))

    valid_agents = Agents.objects.filter(is_available=1, roles__contains=roles)
    count = len(valid_agents)
    error = 0
    if roles == '':
        error = 'Please choose a role'
        response = 'Please Choose a role'

    elif count != 0:
            # # Picking Random Agent
        if mode == 'random':
            agent = choice(valid_agents)

        elif mode == 'least':
            # Whoever is availabe the longest
            agent = min(valid_agents, key=lambda ag: ag.available_since)

        elif mode == 'all':
            # All agents are selected based on profile
            valid_agents = Agents.objects.filter(roles__contains=roles)

            # Agents choose job again a random function
            agent = choice(valid_agents)
        response = agent.allDetail()
        # print(agent.allDetail())
    else:
        error = 'Too Many roles try decreasing number of roles'
        response = 'Too Many roles try decreasing number of roles'

    resMap = {
        "mode": mode,
        "roles": roles,
        'error': error,
        'response': response,
    }
    return JsonResponse(resMap)


def agentReg(request):
    resMap = {}
    available = request.GET.get('available')
    time = request.GET.get('time')
    roles = request.GET.get('roles')
    roles = ' '.join(sorted(roles.split('-')))
    # Agents()
    resMap = {
        'available': available,
        'time': time,
        'roles': roles
    }
    return JsonResponse(resMap)


def insert(request):
    # Automated Data Insertion for use
    # Can be done manually from admin panel
    from random import randint, choices
    insert_enabled = False
    if insert_enabled:
        all_roles = [
            'hr',
            'management',
            'sales',
            'support',
            'technology',
        ]
        for idx in range(100):
            is_available = randint(0, 1)
            h = format(randint(1, 23), '02')
            m = choices(['00', '15', '30', '45'])[0]
            s = '00'
            available_since = f'{h}:{m}:{s}'
            roles = ' '.join(sorted(set(choices(all_roles, k=(idx % 4)+1))))
            print(is_available, available_since, roles)
            a = Agents(is_available=is_available,
                       available_since=available_since, roles=roles)
            a.save()
        return HttpResponse('Sucesss')
    else:
        return HttpResponse('Insert not enabled')
