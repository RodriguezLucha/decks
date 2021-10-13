import React, { useState, useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import {} from './cardSlice'
import { Link } from 'react-router-dom'
import { fetchCardsById, selectAllCards } from './cardSlice'
import { useParams, useHistory } from 'react-router-dom'

export function Card () {
  const cards = useSelector(selectAllCards)
  const dispatch = useDispatch()
  let { id } = useParams()
  useEffect(() => {
    dispatch(fetchCardsById(id))
  }, [])
  let card = cards[0]
  const [showFront, flipCard] = useState(true)

  function frontOfCard (card) {
    return <div dangerouslySetInnerHTML={{ __html: card.front_svg }} />
  }
  function backOfCard (card) {
    return <div dangerouslySetInnerHTML={{ __html: card.back_svg }} />
  }
  let svgContent
  if (showFront) {
    svgContent = frontOfCard()
  } else {
    svgContent = backOfCard()
  }

  return (
    <div>
      <h1>Cards</h1>

      {svgContent}
      <audio controls>
        <source
          src={`http://localhost:5000/decks/${card.deck_id}/cards/${card.id}/file`}
          type='audio/mpeg'
        />
      </audio>
    </div>
  )
}
