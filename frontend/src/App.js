import './App.css';
import './assets/styles/globals.css'
import HomePage from './pages/HomePage';
import ClothingDetailsPage from './pages/ClothingDetailsPage';

import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />,
  },
  {
    path: "roupa/:clothingID/:clothingTitle",
    element: <ClothingDetailsPage />,
  },
]);


function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;
