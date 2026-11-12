# ITWS 4600 Term Project
### Jacob Hebbel

## What is this?
Analysis of specific Kalshi decisions markets and their relationship with more traditional instruments. Specifically focusing on the kalshi FED-DECISIONS event market, which offers contracts on the result the next Federal Reserve interest rate decision. The goal is to see if implied probabilities of this market align with instruments that traditionally act as signals for this decision. Specifically using 30-day US Treasury Futures, Short-term Adjustible Rates, and 2-year Treasury Bond instruments for comparison. The goal is to see if this Kalshi market exhibits no relationship, a lead-lag relationship, or some other relationship with traditional instruments.

## How am I doing this?
I am using the Kalshi API, which keeps historical data through endpoints. For implementation details related to kalshi, see the `kalshi\` folder which I think has some pretty clear code. For traditional instrument prices, I am fortunate enough to have access to a Bloomberg Terminal at my school. My school pays for BLP-API access, granting me programmatic priveliges with the system over a local network. To run analysis, I pull my code onto a terminal and run it there.

## What do the outcomes of this study implicate?
Several things. Kalshi has massively grown as a consumer-oriented retail market, providing a new and exciting exchange that has a significant social presence. According to simple economic theory, actions taken on this exchange should be rational, much like actions taken on traditional exchanges. If so, then a traditional faster exchange may act as an 'oracle' which I could use to inform positionso on the slower Kalshi exchange. Similarly, Kalshi's infrastructure generally forces everyone on the same latency band. While I don't necessarily know if this gives me a direct arbitrage edge, at the very least I am interested in exploring its implications.