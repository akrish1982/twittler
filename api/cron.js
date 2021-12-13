const faunadb = require('faunadb')
const {TwitterApi} = require('twitter-api-v2')

const axios = require('axios');



//const twitterClient = new TwitterApi(process.env.TWITTER_BEARER_TOKEN)
const twitterClient = new TwitterApi({  
  appKey: process.env.API_KEY,  
  appSecret : process.env.API_SECRET,
  accessToken : process.env.ACCESS_TOKEN,
  accessSecret : process.env.ACCESS_TOKEN_SECRET
})
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
      twitterClient.v1.tweet('This tweet was written by a bot').then((val) => {
          console.log(val)
          console.log("success")
      }).catch((err) => {
          console.log(err)
      })
      console.log('I was triggered before posting to twitter')
      // post all tweets from date range on twitter
      data.forEach(async ({data: {tweet}}) => {
        axios({
            method: 'post',
            url: 'https://v1.nocodeapi.com/akrish1982/twitter/NucMmvJBGBEMxGiA?status=' + 'test message', 
            params: {},
        }).then(function (response) {
                // handle success
                console.log(response.data);
        }).catch(function (error) {
                // handle error
                console.log(error);
        })
        console.log('I have data')
        await twitterClient.v1.tweet('I have data')
        console.log('I Tweeted!!!')
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
