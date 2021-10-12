import React from 'react'
import { Deck } from './features/deck/Deck'
import {
  BrowserRouter,
  Switch,
  Route,
  NavLink,
  Redirect
} from 'react-router-dom'

function App () {
  return (
    <div className='App'>
      <BrowserRouter>
        <header>
          <nav>
            <NavLink to='/decks'>Decks</NavLink>
          </nav>
        </header>
        <Switch>
          <Route exact path='/decks' component={Deck} />
        </Switch>
      </BrowserRouter>
    </div>
  )
}

export default App
