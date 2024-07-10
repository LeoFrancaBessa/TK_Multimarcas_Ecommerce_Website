import './App.css';
import './assets/styles/globals.css'
import Home from './pages/Home';

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },
  // {
  //   path: "roupa/:clothingID/:clothingTitle",
  //   element: <Contact />,
  // },
]);


function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;
