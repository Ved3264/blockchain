// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Voting {
    address public admin;
    uint256 public candidateCount;
    uint256 public voterCount;

    struct Candidate {
        uint256 id;
        string name;
        uint256 voteCount;
        bool exists;
    }

    struct Voter {
        uint256 id;
        address wallet;
        string name;
        bool hasVoted;
        bool exists;
    }

    mapping(uint256 => Candidate) public candidates;
    mapping(uint256 => Voter) public voters;
    mapping(address => uint256) public voterIdByAddress;

    event CandidateAdded(uint256 indexed candidateId, string name);
    event VoterAdded(uint256 indexed voterId, address wallet, string name);
    event VoteCast(uint256 indexed voterId, uint256 indexed candidateId);

    modifier onlyAdmin() {
        require(msg.sender == admin, "only admin");
        _;
    }

    constructor() {
        admin = msg.sender;
        candidateCount = 0;
        voterCount = 0;
    }

    function addCandidate(uint256 _candidateId, string calldata _name) external onlyAdmin {
        require(!candidates[_candidateId].exists, "candidate id exists");
        candidates[_candidateId] = Candidate({
            id: _candidateId,
            name: _name,
            voteCount: 0,
            exists: true
        });
        candidateCount += 1;
        emit CandidateAdded(_candidateId, _name);
    }

    function addVoter(uint256 _voterId, address _wallet, string calldata _name) external onlyAdmin {
        require(!voters[_voterId].exists, "voter id exists");
        require(_wallet != address(0), "invalid wallet");
        require(voterIdByAddress[_wallet] == 0, "wallet already registered");
        voters[_voterId] = Voter({
            id: _voterId,
            wallet: _wallet,
            name: _name,
            hasVoted: false,
            exists: true
        });
        voterIdByAddress[_wallet] = _voterId;
        voterCount += 1;
        emit VoterAdded(_voterId, _wallet, _name);
    }

    function castVote(uint256 _voterId, uint256 _candidateId) external {
        require(voters[_voterId].exists, "voter not found");
        require(candidates[_candidateId].exists, "candidate not found");
        require(msg.sender == voters[_voterId].wallet, "caller not voter wallet");
        require(!voters[_voterId].hasVoted, "already voted");
        voters[_voterId].hasVoted = true;
        candidates[_candidateId].voteCount += 1;
        emit VoteCast(_voterId, _candidateId);
    }

    function getCandidate(uint256 _candidateId) external view returns (uint256, string memory, uint256) {
        require(candidates[_candidateId].exists, "candidate not found");
        Candidate storage c = candidates[_candidateId];
        return (c.id, c.name, c.voteCount);
    }

    function getVoter(uint256 _voterId) external view returns (uint256, address, string memory, bool) {
        require(voters[_voterId].exists, "voter not found");
        Voter storage v = voters[_voterId];
        return (v.id, v.wallet, v.name, v.hasVoted);
    }

    function counts() external view returns (uint256 _candidates, uint256 _voters) {
        return (candidateCount, voterCount);
    }
}
