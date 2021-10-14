import React, { useState, useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import {} from './cardSlice'
import { Link } from 'react-router-dom'
import { fetchCardsById, toggleCardById, selectAllCards } from './cardSlice'
import { useParams, useHistory } from 'react-router-dom'

export function Card () {
  const cards = useSelector(selectAllCards)
  const dispatch = useDispatch()
  let { id } = useParams()
  useEffect(() => {
    dispatch(fetchCardsById(id))
  }, [JSON.stringify(cards)])

  const [showFront, flipCard] = useState(true)
  const [showHiddenFront, flipHiddenCard] = useState(true)

  let shownCards = cards.filter(c => !c.hidden)
  let hiddenCards = cards.filter(c => c.hidden)

  let card = null
  let hiddenCard = null

  if (shownCards) {
    card = shownCards[0]
  }
  if (hiddenCards) {
    hiddenCard = hiddenCards[0]
  }

  function frontOfCard (card) {
    if (card) {
      return <div dangerouslySetInnerHTML={{ __html: card.front_svg }} />
    }
    return null
  }
  function backOfCard (card) {
    if (card) {
      return <div dangerouslySetInnerHTML={{ __html: card.back_svg }} />
    }
    return null
  }
  function audioClip (card) {
    if (card) {
      return (
        <audio controls>
          <source
            src={`http://localhost:5000/decks/${card.deck_id}/cards/${card.id}/file`}
            type='audio/mpeg'
          />
        </audio>
      )
    }
    return null
  }

  return (
    <div className='cardHolder'>
      <div className='card'>
        <button onClick={() => flipCard(!showFront)}>Flip</button>
        <button onClick={() => dispatch(toggleCardById(card))}>Toggle</button>

        {showFront ? frontOfCard(card) : backOfCard(card)}
        {!showFront ? audioClip(card) : null}
      </div>
      <div className='hiddenCard'>
        <button onClick={() => flipHiddenCard(!showHiddenFront)}>Flip</button>
        <button onClick={() => dispatch(toggleCardById(hiddenCard))}>
          Toggle
        </button>

        {showHiddenFront ? frontOfCard(hiddenCard) : backOfCard(hiddenCard)}
        {!showHiddenFront ? audioClip(hiddenCard) : null}
      </div>
    </div>
  )
}
