const faunadb = require('faunadb')
const {TwitterApi} = require('twitter-api-v2')

const twitterClient = new TwitterApi(process.env.TWITTER_BEARER_TOKEN)

const q = faunadb.query

const faunaClient = new faunadb.Client({
  secret: process.env.REACT_APP_FAUNADB_SECRET,
})

module.exports = async (req, res) => {
  if (req.method === 'POST') {
    console.log('I was triggered during POST method')
    try {
      const now = new Date()
      now.setSeconds(0)
      now.setMilliseconds(0)

      console.log('I was triggered before fauna query')
      // get all tweets from Now - 1 minute to Now
      const {data} = await faunaClient.query(
        q.Map(
          q.Paginate(q.Match(q.Index('tweetsByDate'), now.getTime())),
          q.Lambda(['date', 'ref'], q.Get(q.Var('ref')))
        )
      )
    
      console.log('I was triggered before posting to twitter')
      // post all tweets from date range on twitter
      data.forEach(async ({data: {tweet}}) => {
        await twitterClient.v1.tweet(tweet)
      })
      res.status(200).json({success: true})
    } catch (err) {
      res.status(500).json({statusCode: 500, message: err.message})
    }
  } else {
    res.setHeader('Allow', 'POST')
    res.status(405).end('Method Not Allowed')
  }
}
