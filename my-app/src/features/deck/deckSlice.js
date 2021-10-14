import {
  createSlice,
  createAsyncThunk,
  createEntityAdapter
} from '@reduxjs/toolkit'
import { v1 as uuid } from 'uuid'
import _ from 'lodash'
import { normalize } from 'normalizr'
import { deckSchema } from '../../schema.js'

export const fetchDecks = createAsyncThunk(
  'deck/fetchDecks',
  async thunkApi => {
    const response = await fetch(`decks/`)
    const data = await response.json()
    const normalized = normalize(data, { data: [deckSchema] })
    return { entities: normalized.entities }
  }
)

const deckAdapter = createEntityAdapter()

export const deckSlice = createSlice({
  name: 'deck',
  initialState: deckAdapter.getInitialState(),
  reducers: {},
  extraReducers: {
    [fetchDecks.fulfilled]: (state, action) => {
      deckAdapter.upsertMany(state, action.payload.entities.deck)
    }
  }
})

export const {} = deckSlice.actions

export const {
  selectById: selectDeckById,
  selectIds: selectDeckIds,
  selectEntities: selectDeckEntities,
  selectAll: selectAllDecks,
  selectTotal: selectTotalDecks
} = deckAdapter.getSelectors(state => state.deck)

export default deckSlice.reducer
