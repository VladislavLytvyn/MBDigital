from annoying.decorators import render_to


@render_to('homepage.html')
def homepage(request):
    return {'persons_url': request.path + 'persons', 'groups_url': request.path + 'groups'}
