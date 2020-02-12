# alternative_trips

This is a project I've started at the Kiwi Hackathon Barcelona 2019.

The initial commit was all I did in the 24h Hackathon.

The idea was to generate a random route based on an initial set point with different params like difficulty (a combination of elevation and distance) and location. We didn't manage to finish the integration in time with the frontend due to lack of consistency of GMaps data integration but the gist is as follows:
- Get Nearby Interest Points from the GMaps Nearby API from an initial location set point away from the city
- Set a course of random routes with the highest rated places within the difficulty constrains
- Get more detailed data about the points in the route like reviews and pictures from the GMaps Places API
- Feed all this information to be displayed on a map on the frontend with extra information about the points
