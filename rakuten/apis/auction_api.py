from .base_api import BaseApi


class AuctionItemApi(BaseApi):
    def search(self, **kwargs):
        return self._request(
            '/AuctionItem/Search/20130905',
            kwargs,
            self._parse_auctions_result
        )

    def _parse_auctions_result(self, result):
        return [self._parse_auction_item(r) for r in result['Items']]

    def _parse_auction_item(self, item_info):
        return item_info['Item']
