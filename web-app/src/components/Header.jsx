import { Link, Route, BrowserRouter as Router, Switch } from 'react-router-dom'

const Header = () =>{
    return(
            <div class="navbar navbar-expand-lg ">
                {/* <a class="navbar-brand" href="#">Navbar</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button> */}
                <div class="collapse navbar-collapse" id="navbarNav">
                    <Router>
                        <ul class="navbar-nav">
                            <li class="nav-item">
                                <Link class="nav-link" to="/">Home</Link> 
                            </li>
                            {/* <li class="nav-item">
                                <a class="nav-link" href="#"></a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Pricing</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Disabled</a>
                            </li> */}
                        </ul>
                    </Router>
                </div>
            </div>
    )
}

export default Header;