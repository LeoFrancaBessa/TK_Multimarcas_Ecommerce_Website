import './App.css';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import './assets/styles/globals.css'
import HomePage from './pages/HomePage';
import ClothingDetailsPage from './pages/ClothingDetailsPage';
import ClothingSearchingPage from './pages/ClothingSearchingPage';
import { createBrowserRouter, RouterProvider} from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />,
  },
  {
    path: "roupa/:clothingID/:clothingTitle",
    element: <ClothingDetailsPage />,
  },
  {
    path: "busca/:clothingTitle",
    element: <ClothingSearchingPage />,
  }
]);


function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;
