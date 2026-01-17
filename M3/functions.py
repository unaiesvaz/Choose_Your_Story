def get_answers_bystep_adventure():
    from variables import idAnswers_ByStep_Adventure
    return idAnswers_ByStep_Adventure
def get_adventures_with_chars():
    from variables import ADVENTURES
    return ADVENTURES
def get_id_bystep_adventure():
    from variables import id_by_steps
    return id_by_steps
def get_first_step_adventure(id_adventure):
    from variables import FIRST_STEP_BY_ADVENTURE
    return FIRST_STEP_BY_ADVENTURE[id_adventure]
def get_characters():
    from variables import CHARACTERS
    return CHARACTERS
# getReplayAdventures()
# getChoices()
# getIdGames()
# insertCurrentGame(idGame,idUser,isChar,idAdventure)
def getUsers():
    from variables import USERS
    return USERS
def getUserIds():
    lista_users = []
    lista_ids = list(getUsers().keys())
    for clave in lista_ids:
        lista_users.append(getUsers()[clave]["username"])
    return [lista_users]+[lista_ids]

# insertUser(id, user, password)
# get_table(query)
def userExists(user):
    lista = getUserIds()
    if user not in lista[0]:
        return False
    else:
        return True

def checkUserbdd(user, password): # AQUI ERROR
    var = userExists(user)
    if not var:
        return 0
    if password != getUsers()[user]["password"]:
        return -1
    return 1

# setIdGame()
# insertCurrentChoice(idGame, actual_id_step, id_answer)
# formatText(text, lenLine, split)
def getHeader(text):
    header = "*".center(80,"*") + "\n" + text.center(80,"=") + "\n" + "*".center(80,"*") + "\n"
    return header
# getFormatedBodyColumns(tupla_texts, tupla_sizes, margin=0)
# getFormatedAdventures(adventures)
# getFormatedAnswers(idAnswer, text, lenLine, leftMargin)
# getHeadeForTableFromTuples(t_name_columns, t_size_columns, title="")
# getTableFromDict(tuple_of_keys, weigth_of_columns, dict_of_data)
# getOpt(textOpts="", inputOptText="", rangeList=[], dictionary={}, exceptions=[])
# getFormatedTable(queryTable, title="")
# checkPassword(password)
#def checkUser(user):
# replay(choices)


