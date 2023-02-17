from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

albums_blueprint = Blueprint("albums", __name__)