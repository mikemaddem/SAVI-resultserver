from quart import Quart, render_template, request

from .ballotserver_utils import challenge_ballot, get_election_results


app = Quart(__name__)


@app.route("/")
async def home():
    """
    Home page, welcome

    Returns:
        Rendered template of homepage
    """
    return await render_template('home.html')


@app.route("/results")
async def results():
    """
    Query the ballotserver for the election results

    Returns:
        Rendered template of the results page
    """
    results = get_election_results()
    return await render_template('results.html', results=results)


@app.route("/challenge", methods=["GET", "POST"])
async def challenge():
    """
    Querry the ballotserver by verification code to challenge a spoiled ballot

    Returns:
        Rendered template of challenged ballot or blank if failed
    """
    if request.method == "GET":
        return await render_template("challenge.html")
    elif request.method == "POST":
        form = await request.form
        try:
            verification_code = form["verification_code"]
            challenged = challenge_ballot(verification_code)
            if challenged:
                return await render_template("challenge.html", ballot=challenged)
            else:
                return await render_template("challenge.html", error="Verification code does not match a spoiled ballot")
        except KeyError:
            return await render_template("challenge.html", error="Verification code is required")
