import './App.css';
import './assets/styles/globals.css'
import FirstHeader from './components/headers/FirstHeader/FirstHeader'
import SecondHeader from './components/headers/SecondHeader/SecondHeader';
import SectionsTitle from './components/commons/SectionsTitle/SectionsTitle';

function App() {
  return (
    <div className="App">
      <FirstHeader phone={"(98) 98419-0129"} email={"tkmultimarcas@gmail.com"}/>
      <SecondHeader/>
      <SectionsTitle text={"Destaques"} />
    </div>
  );
}

export default App;
