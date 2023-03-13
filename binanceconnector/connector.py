##Documento de configuracion del token Binance
import config

##Python
from pprint import pprint

##Pandas
import pandas as pd

##Binance-connector
from binance.spot import Spot


class RobotBinance:
    """
    Bot para binance en spot, compra y venta
    """
    __api_key = config.API_KEY
    __api_secret = config.API_SECET_KEY
    binance_client = Spot(key=__api_key ,secret=__api_secret)

    def __init__(self):
        pass

    def _request(self, endpoint:str, parameters=None):
        while True:    
            try:
                response = getattr(self.binance_client, endpoint)
                return response() if parameters is None else response(**parameters)
            except:
                print("Not conexion")
                break

    def binance_account(self):            
        """ 
        Return metrics and account balance
        """        
        return self._request("account")

    def cryptocurriencies(self):
        """ 
        Return al cryptocurriencies avaliable on account
        """
        return [crypto for crypto in self.binance_account().get("balances") if float(crypto.get("free")) > 0]  
        

    def symbol_price(self):        
        """
        Return prices for the criptocurriencies:
        (btcusdt,solusdt)
        """
        criptos =pd.DataFrame(self._request("ticker_price"), columns=["symbol","price"])
        return criptos
        
         

if __name__=="__main__":
    bot= RobotBinance()
    pprint(bot.symbol_price())



