import { configureStore } from '@reduxjs/toolkit'
import deck from '../features/deck/deckSlice'
import card from '../features/card/cardSlice'
import throttle from 'lodash/throttle'
export default configureStore({
  reducer: {
    deck,
    card
  }
})
