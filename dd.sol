// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.17;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/math/SafeMath.sol";

contract RealState {
    using SafeMath for uint256;

    struct Property {
        uint256 price;
        address owner;
        bool forSale;
        string name;
        string description;
        string location;
    }

    mapping(uint256 => Property) properties;
    uint256[] public propertyIds;
    event propertySold(uint256 propertyId);

    function getProperty(
        uint256 propertyId
    )
        public
        view
        returns (
            uint,
            address,
            bool,
            string memory,
            string memory,
            string memory
        )
    {
        Property storage property = properties[propertyId];
        require(property.owner == msg.sender, "you aren't owner");
        return (
            property.price,
            property.owner,
            property.forSale,
            property.name,
            property.description,
            property.location
        );
    }

    function listPropertyForSale(
        uint256 _propertyId,
        uint256 _price,
        string memory _name,
        string memory _description,
        string memory _location
    ) public {
        Property memory newProperty = Property({
            price: _price,
            owner: msg.sender,
            forSale: true,
            name: _name,
            description: _description,
            location: _location
        });

        properties[_propertyId] = newProperty;
        propertyIds.push(_propertyId);
    }

    function buyProperty(uint256 _propertyId) public payable {
        Property storage property = properties[_propertyId];
        require(property.owner != msg.sender, " you are Property owner ");
        require(property.forSale, "Property isn't for sale");
        require(property.price <= msg.value, " Insufficient funds");
        property.owner = msg.sender;
        property.forSale = false;
        payable(property.owner).transfer(property.price);
        emit propertySold(_propertyId);
    }
}
