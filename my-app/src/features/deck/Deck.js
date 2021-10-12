import React, { useState, useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import {} from './deckSlice'
import { Link } from 'react-router-dom'
import { fetchDecks, selectAllDecks } from './deckSlice'

export function Deck () {
  const decks = useSelector(selectAllDecks)
  const dispatch = useDispatch()
  useEffect(() => {
    dispatch(fetchDecks())
  }, [])
  console.log(decks)

  return (
    <div>
      <h1>Decks</h1>
      {decks.map(d => {
        return <div key={d.id}>{d.name}</div>
      })}
    </div>
  )
}
