from sys import modules
import wolframalpha


def calculator(query):
    app_id = 'LU92R9-JTKAWAWXAP'
    client = wolframalpha.Client(app_id)
    indx = query.lower().split().index('calculate')
    query = query.split()[indx + 1:]
    res = client.query(' '.join(query))
    answer = next(res.results).text

    return answer

modules[__name__] = calculator