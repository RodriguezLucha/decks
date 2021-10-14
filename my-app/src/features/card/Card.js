import React, { useState, useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import {} from './cardSlice'
import {
  fetchCardsById,
  toggleCardById,
  selectAllCards,
  selectCardEntities,
  selectCardIds
} from './cardSlice'
import { useParams } from 'react-router-dom'

export function Card () {
  const cards = useSelector(selectAllCards)
  const cardEntities = useSelector(selectCardEntities)

  console.log(cardEntities)

  const dispatch = useDispatch()
  let { id } = useParams()
  const stringifiedCards = JSON.stringify(cards)

  const [shownIds, setShownIds] = useState(
    cards.filter(c => !c.hidden).map(c => c.id)
  )
  const [hiddenIds, setHiddenIds] = useState(
    cards.filter(c => c.hidden).map(c => c.id)
  )

  function updateStates (cards) {
    setShownIds(cards.filter(c => !c.hidden).map(c => c.id))
    setHiddenIds(cards.filter(d => d.hidden).map(d => d.id))
  }

  function advanceShownCard () {
    let copy = [...shownIds]
    let first = copy.shift()
    copy.push(first)
    setShownIds(copy)
  }
  function advanceHiddenCard () {
    let copy = [...hiddenIds]
    let first = copy.shift()
    copy.push(first)
    setHiddenIds(copy)
  }

  useEffect(() => {
    dispatch(fetchCardsById(id)).then(() => updateStates(cards))
  }, [stringifiedCards])

  const [showFront, flipCard] = useState(true)
  const [showHiddenFront, flipHiddenCard] = useState(true)

  let card = null
  let hiddenCard = null

  if (shownIds) {
    let cardList = shownIds.map(id => cardEntities[id])
    card = cardList[0]
  }
  if (hiddenIds) {
    let cardList = hiddenIds.map(id => cardEntities[id])
    hiddenCard = cardList[0]
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
        <button onClick={() => advanceShownCard()}>Next</button>
        <button onClick={() => dispatch(toggleCardById(card))}>Toggle</button>

        {showFront ? frontOfCard(card) : backOfCard(card)}
        {!showFront ? audioClip(card) : null}
      </div>
      <div className='hiddenCard'>
        <button onClick={() => flipHiddenCard(!showHiddenFront)}>Flip</button>
        <button onClick={() => advanceHiddenCard()}>Next</button>
        <button onClick={() => dispatch(toggleCardById(hiddenCard))}>
          Toggle
        </button>

        {showHiddenFront ? frontOfCard(hiddenCard) : backOfCard(hiddenCard)}
        {!showHiddenFront ? audioClip(hiddenCard) : null}
      </div>
    </div>
  )
}
