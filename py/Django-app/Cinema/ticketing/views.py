from cgitb import html
from html.entities import html5
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from ticketing.models import Movie, Cinema, ShowTime


# view of url movie/list with name movie_list
def movie_list(request):
    # query for return all objects in Movie model
    movies = Movie.objects.all()
    # count all objects in Movie model
    count = len(movies)
    # context of render function for show data in template of view (for path movie/list)
    context = {
        'movie_list': movies,
        'movie_count': count
    }
    return render(request, 'ticketing/movielsit.html', context)
    # return response for request with template file and data(with template : movielist.html)

    # response_text = '\n'.join('{} : {}'.format(i, movie) for i, movie in enumerate(movies, start=1))
    # return HttpResponse(str(response_text))


# view of url cinema/list with name cinema_list
def cinema_list(request):
    # query for return all objects in Cinema model
    cinemas = Cinema.objects.all()
    # count all objects in Movie model
    count = len(cinemas)
    # context of render function for show data in template of view (for path cinema/list)
    context = dict(cinema_list=cinemas, cinema_count=count)
    # return response for request with template file and data(with template : cinemalist.html)
    return render(request, "ticketing/cinemalist.html", context)


def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'ticketing/movie_details.html', context)


def cinema_details(request, cinema_id):
    cinemas = get_object_or_404(Cinema, pk=cinema_id)
    context = {
        'cinema': cinemas
    }
    return render(request, 'ticketing/cinema_details.html', context)


def showtime_list(request):
    showtime = ShowTime.objects.all()
    context = {
        "showtimes": showtime
    }
    return render(request, "ticketing/showtime_list.html", context)
    # response_text = """
    # <!DOCTYPE html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #     <title>سینما ها</title>
    # </head>
    # <body>
    #
    #     <h1>سینما های کشور</h1>
    #     <ul>
    #         {}
    #     </ul>
    #
    # </body>
    # </html>
    # """.format('\n'.join('<li>{}</li>'.format(cinema) for cinema in cinemas))
    # return HttpResponse(response_text)
