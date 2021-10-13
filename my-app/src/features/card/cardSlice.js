import {
  createSlice,
  createAsyncThunk,
  createEntityAdapter
} from '@reduxjs/toolkit'
import { v1 as uuid } from 'uuid'
import _ from 'lodash'
import { normalize } from 'normalizr'
import { cardSchema } from '../../schema.js'

export const fetchCardsById = createAsyncThunk(
  'card/fetchCardsById',
  async (deck_id, thunkApi) => {
    const response = await fetch(`http://localhost:5000/decks/${deck_id}/cards/`)
    const data = await response.json()
    const normalized = normalize(data, { data: [cardSchema] })
    return { entities: normalized.entities }
  }
)

const cardAdapter = createEntityAdapter()

export const cardSlice = createSlice({
  name: 'card',
  initialState: cardAdapter.getInitialState(),
  reducers: {},
  extraReducers: {
    [fetchCardsById.fulfilled]: (state, action) => {
      cardAdapter.upsertMany(state, action.payload.entities.card)
    }
  }
})

export const {} = cardSlice.actions

export const {
  selectById: selectCardById,
  selectIds: selectCardIds,
  selectEntities: selectCardEntities,
  selectAll: selectAllCards,
  selectTotal: selectTotalCards
} = cardAdapter.getSelectors(state => state.card)

export default cardSlice.reducer
