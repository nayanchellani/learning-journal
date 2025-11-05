import Home from "./Home";
import Dashboard from "./Dashboard";
import About from "./About";
import { Link } from "react-router-dom";
import './App.css' 

const Navbar = () => {
  return (
    <nav>
        <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/dashboard">Dashboard</Link></li>
            <li><Link to="/about">About</Link></li>
             
             
        </ul>   
        <button className="holo-btn">pitch</button>
    </nav>
  );
}
export default Navbar;