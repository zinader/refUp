import { Link, Route, BrowserRouter as Router, Switch } from 'react-router-dom'
import panelImg from './assets/panel-img.png'
import Employee from './Employee'
import Programs from './Programs'
import Referals from './Referals'

const Panel = () => {
    return(
        <Router>
        <div className='panel'>
            <div className='row'>
                <div className='col-md-7 col-12'>
                    <div className='panel-heading'>
                        <p>
                            All opportunities at one place.
                        </p>
                        <h1>
                            refup.
                        </h1>
                    </div>
                    <div className='navigator'>
                        <div className='programs-btn'>
                            <Link to="/referals">Referals</Link>
                        </div>
                        <div className='remote-btn'>
                            <Link to="/programs">Student Programs</Link>
                        </div>
                    </div>
                </div>
                <div className='col-md-5 col-12'>
                    <div className='panel-img'>
                        <img width='80%' src={panelImg} />
                    </div>
                </div>
            </div>
            {/* <div className='search-area'>
                <div className='row'>
                    <div className='col-md-4 col-8'>
                        <div className='search'>
                            <input placeholder='Search for a keyword..' id='query' name='query'></input>
                        </div>
                    </div>
                    <div className='offset-5 col-md-3 col-4'>
                        <div className='submit'>
                            <button type='submit'>Search</button>
                        </div>
                    </div>
                </div>
            </div> */}
                <Switch>
                    <Route path="/referals">
                        <Referals />
                    </Route>
                    <Route path="/programs">
                        <Programs />
                    </Route>
                    <Route path="/applicants">
                        <Employee />
                    </Route>
                </Switch>
        </div>
        </Router>
    )
}

export default Panel