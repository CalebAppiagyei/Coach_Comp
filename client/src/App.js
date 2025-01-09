import './App.css';
import { BrowserRouter as Router, Route, Routes} from "react-router-dom";  


function App() {
  return (
    <Router>
      {/* Routes */}
      <Routes>
        <Route
          path='/'
          element={
              <>
                <h1>Welcome to Coach Compare</h1>
              </>
          }
        />
        <Route
          path='/search'
          element={
            <>
              <h1>Search page</h1>
            </>
        }
        />
        <Route
          path='/compare'
          element={
            <>
              <h1>Compare page</h1>
            </>
        }
        />
        <Route
          path='/contribute'
          element={
            <>
              <h1>Contribute page</h1>
            </>
        }
        />
      </Routes>
    </Router>
  );
}

export default App;
