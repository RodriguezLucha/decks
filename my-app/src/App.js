import React from 'react'
import { Deck } from './features/deck/Deck'
import { Card } from './features/card/Card'
import { BrowserRouter, Switch, Route, NavLink } from 'react-router-dom'

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
          <Route exact path='/decks/:id/card' component={Card} />
        </Switch>
      </BrowserRouter>
    </div>
  )
}

export default App
