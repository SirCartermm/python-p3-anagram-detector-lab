from anagram import Anagram

def test_detect_anagrams():
    detector = Anagram("ant")
    anagrams = detector.match(["tan", "ant", "abc", "nat", "bat", "cat"])
    assert set(anagrams) == set(["tan", "nat"]), f"Expected ['tan', 'nat'] but got {anagrams}"
    print("Test 1: PASS")

    detector = Anagram("listen")
    anagrams = detector.match(["enlist", "google", "inlets", "banana"])
    assert set(anagrams) == set(["inlets"]), f"Expected ['inlets'] but got {anagrams}"
    print("Test 2: PASS")

    detector = Anagram("master")
    anagrams = detector.match(["stream", "pines", "mastre", "hammer", "tamas"])
    assert set(anagrams) == set(["stream", "mastre"]), f"Expected ['stream', 'mastre'] but got {anagrams}"
    print("Test 3: PASS")

    detector = Anagram("good")
    anagrams = detector.match(["dog", "goody"])
    assert set(anagrams) == set(["goody"]), f"Expected ['goody'] but got {anagrams}"
    print("Test 4: PASS")

test_detect_anagrams()