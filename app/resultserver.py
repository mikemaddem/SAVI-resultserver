from quart import Quart, abort, redirect, render_template, url_for

from .ballotserver_utils import get_election_results


app = Quart(__name__)


@app.route("/")
async def home():
    """
    Redirect to the results page

    Returns:
        redirect to the results page
    """
    return redirect(url_for('results'))


@app.route("/results")
async def results():
    """
    Query the ballotserver for the election results

    Returns:
        Rendered template of the results page
    """
    results = get_election_results()
    return await render_template('results.html', results=results)


@app.route("/challenge")
async def challenge():
    # TODO
    abort(501)
